from flask import render_template, Blueprint, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator


translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        languages = LanguageModel.list_dicts()
        text_to_translate = request.form["text-to-translate"]
        translate_from = request.form["translate-from"]
        translate_to = request.form["translate-to"]

        translated = GoogleTranslator(source=translate_from,
                                      target=translate_to).translate(
                                      text=text_to_translate
                                  )

        return render_template("index.html",
                               languages=languages,
                               text_to_translate=text_to_translate,
                               translate_from=translate_from,
                               translate_to=translate_to,
                               translated=translated)
    else:
        languages = LanguageModel.list_dicts()
        text_to_translate = "O que deseja traduzir?"
        translate_from = "pt"
        translate_to = "en"
        translated = "What do you want to translate?"
        return render_template("index.html",
                               languages=languages,
                               text_to_translate=text_to_translate,
                               translate_from=translate_from,
                               translate_to=translate_to,
                               translated=translated)
