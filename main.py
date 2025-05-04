import json
import locale
from functools import lru_cache
from pathlib import Path
from typing import Any, Final, Literal

from babel.support import Translations
from cssmin import cssmin
from jinja2 import Environment, PackageLoader, select_autoescape

type Language = Literal["en", "ua"]
type CVSection = Literal["main", "about", "experience", "education", "languages", "social"]

supported_languages: Final[set[Language]] = {"en", "ua"}
main_language: Final[Language] = "en"
locales: Final[dict[Language, str]] = {
    "en": "en",
    "ua": "uk",
}
cv_sections_data_source: dict[CVSection, str] = {
    "main": "src/data/main.json",
    "about": "src/data/about.json",
    "experience": "src/data/experience.json",
    "education": "src/data/education.json",
    "languages": "src/data/languages.json",
    "social": "src/data/social.json",
}


@lru_cache(maxsize=128)
def _read_json_file(file_path: str) -> dict[Language, Any]:
    with Path.open(Path(file_path), encoding="utf-8") as f:
        return json.load(f)


def _get_cv_chapter_data(chapter: CVSection) -> dict[Language, Any]:
    return _read_json_file(cv_sections_data_source[chapter])


def _get_css() -> str:
    with Path.open(Path("./styles.css"), encoding="utf-8") as f:
        css = f.read()

    return cssmin(css)

def _get_langs_data(page_lang: Language) -> list[dict]:
    return [{
        "title": language.upper(),
        "url": f"{language}.html" if language != main_language else "index.html",
        "class": "active" if language == page_lang else ""
    } for language in supported_languages]


def main() -> None:
    env = Environment(
        loader=PackageLoader("src"),
        autoescape=select_autoescape(),
        extensions=["jinja2.ext.i18n"],
    )

    template = env.get_template("index.html")

    default_locale = locale.setlocale(locale.LC_ALL)
    for lang in supported_languages:
        translations = Translations.load("locale", locales[lang])
        env.install_gettext_translations(translations)

        result = template.render(
            main_items=_get_cv_chapter_data("main")[lang],
            about_items=_get_cv_chapter_data("about")[lang],
            experience_items=_get_cv_chapter_data("experience")[lang],
            education_items=_get_cv_chapter_data("education")[lang],
            language_items=_get_cv_chapter_data("languages")[lang],
            social_links_items=_get_cv_chapter_data("social")[lang],
            inline_css=_get_css(),
            language=lang,
            languages=_get_langs_data(lang),
        )

        dest = "dist/index.html" if lang == main_language else f"dist/{lang}.html"
        with Path.open(Path(dest), "w", encoding="utf-8") as f:
            f.write(result)

    locale.setlocale(locale.LC_ALL, default_locale)


if __name__ == "__main__":
    main()
