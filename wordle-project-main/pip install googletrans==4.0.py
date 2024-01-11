'''
from googletrans import Translator, LANGUAGES

def is_valid_word(word):
    translator = Translator()

    try:
        detected_language = translator.detect(word).lang

        print(f"{word}의 언어는 {LANGUAGES[detected_language]}입니다.")

        if detected_language in ['ko', 'en']:
            translation = translator.translate(word, src=detected_language, dest=detected_language)
            if translation.text.lower() == word.lower():
                print(f"{word}은(는) 실제로 존재하는 단어입니다.")
            else:
                print(f"{word}은(는) 사전에 없는 단어입니다.")
        else:
            print("영어 또는 한글이 아닌 다른 언어입니다.")

    except Exception as e:
        print(f"오류 발생: {e}")

# 사용자로부터 단어를 입력받음
user_input = input("단어를 입력하세요: ")
is_valid_word(user_input)
'''

from googletrans import Translator, LANGUAGES

def is_valid_english_word(word):
    translator = Translator()

    try:
        # 입력된 단어의 언어를 감지
        detected_language = translator.detect(word).lang

        # 만약 언어가 영어이면서 번역된 결과가 존재하는 경우, 실제 단어로 판별
        if detected_language == 'en':
            translation = translator.translate(word, src=detected_language, dest=detected_language)
            return translation.text.lower() == word.lower()

    except Exception as e:
        print(f"오류 발생: {e}")

    # 언어가 영어가 아니거나 예외가 발생한 경우에는 False를 반환
    return False

# 사용자로부터 단어를 입력받음
user_input = input("영어 단어를 입력하세요: ")

# 함수 호출 및 결과 출력
result = is_valid_english_word(user_input)
if result:
    print(f"{user_input}은(는) 영어 사전에 실제로 존재하는 단어입니다.")
    print(result)
else:
    print(f"{user_input}은(는) 영어 사전에 존재하지 않는 단어이거나 영어가 아닌 언어일 수 있습니다.")
    print(result)
