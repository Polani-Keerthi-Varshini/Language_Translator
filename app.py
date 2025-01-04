from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from googletrans import LANGUAGES

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    translated_text = ""
    error_message = ""
    if request.method == 'POST':
        try:
            source_text = request.form['source_text']
            src_lang = request.form['src_lang']
            dest_lang = request.form['dest_lang']
            
            # Perform translation with Deep-Translator
            translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(source_text)
        except Exception as e:
            error_message = f"Error: {str(e)}"

    languages = LANGUAGES
    return render_template('index.html', languages=languages, translated_text=translated_text, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)

