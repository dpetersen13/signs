from vulavula import VulavulaClient

def convert_lang_code(lang_code):
  lang_mapping = {
    "nso_Latn": "sepedi",
    "afr_Latn": "afrikaans",
    "sot_Latn": "sesotho",
    "ssw_Latn": "siswati",
    "tso_Latn": "xitsonga",
    "tsn_Latn": "setswana",
    "xho_Latn": "isixhosa",
    "zul_Latn": "isizulu",
    "eng_Latn": "english",
    "swh_Latn": "swahili"
  }
  return lang_mapping.get(lang_code, lang_code)

def translate_from_box():  


    # Define the translation data
    translation_data = {
    "input_text": "begin working now please ." , 
    "source_lang": ("eng_Latn"),
    "target_lang": ("zul_Latn")
    }

    source_lang = convert_lang_code(translation_data['source_lang'])
    target_lang = convert_lang_code(translation_data['target_lang'])

    translation_result = client.translate(translation_data)
    # spoken_text = translation_result['translation'][0]['translation_text']
    spoken_text = translation_result['translation'][0]['translated_text']

    print(f"Your text, '{translation_data['input_text']}' translated from {source_lang} may be translated into {target_lang} as '{ spoken_text}' ")

translate_from_box()





