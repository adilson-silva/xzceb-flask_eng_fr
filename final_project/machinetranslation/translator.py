import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def translate(text, model_id):
    """Translate text using whatson language translator."""
    if not text:
        return None
    try:
        return language_translator.translate(text=text,
            model_id=model_id).get_result()['translations'][0]['translation']
    except Exception:
        return None

def english_to_french(english_text):
    """Translate from english to french."""
    return translate(english_text, 'en-fr')

def french_to_english(french_text):
    """Translate from french to english."""
    return translate(french_text, 'fr-en')
