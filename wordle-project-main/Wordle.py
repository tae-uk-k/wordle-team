import pandas as pd
import random
from googletrans import Translator, LANGUAGES

class Wordle:
    df = pd.read_excel("./단어장전처리.xlsx", sheet_name="vocList", header = None)
    difficulty = 0
    difficultyArea = [[3, 4, 5, 6], [7, 8, 9], [10, 11, 12, 13, 14, 15, 16]]
    keyword = ""
    wordLength = 0
    lastTurn = 0
    
    def getTurn(self):
        return self.lastTurn

    def setDifficulty(self, num):
        self.difficulty = int(num)

    def checkMatch(self, l, str, size):
        for i in range(size):
            if l[i] != str[i]:
                return False
        return True

    def __init__(self):
        df = pd.read_excel("./단어장전처리.xlsx", sheet_name="vocList", header = None)
        #생성자, 뭘 넣어야 할지 모르겠음
    
    def getRandomKeyword(self):
        lengthList = []
        lengthSum = 0
        for v in self.difficultyArea[self.difficulty]:
            lengthList.append(self.df[v - 1][0])
            lengthSum += self.df[v - 1][0]
        randomNumber = random.randrange(0, lengthSum - 1)
        
        for i in range(len(self.difficultyArea[self.difficulty])):
            if (randomNumber > lengthList[i]):
                randomNumber -= lengthList[i]
                continue
            else:
                self.keyword = self.df[i + self.difficultyArea[self.difficulty][0] - 1][randomNumber + 1]
                try:#nan 값이 뜰 수 있을까봐.....
                    self.wordLength = len(self.keyword)
                except:
                    print("에러ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ")
                    self.getRandomKeyword()
                break
            #keyword를 임의화 시켰는데 여전히 범위가 맞는지 확신하지 못하겠음.....
        
    def preSetting(self):
        self.getRandomKeyword()


    def gamePlay(self):
        print(self.keyword, "!!!!!!!!!!!!!!!!!!!!!")
        inputWord = [[' ' for j in range(self.wordLength)] for i in range(self.wordLength + 1)]
        wordStatus = [[0 for j in range(self.wordLength)] for i in range(self.wordLength + 1)]    # 0 - 미입력, 1 - 없음, 2 - 있지만 자리가 다름, 3 - 자리까지 같음
        turn = 0
        gameWin = False
        gameLose = False
        print("wordle game start!!!")
        while(not (gameWin or gameLose)):#전체 게임 루프
            turn += 1
            
            #입력부
            while(True):
                if (turn > self.wordLength + 1):
                    gameLose = True
                    break
                while(True):
                    ans = input("영단어를 입력하세요>>")
                    ans = ans.lower()
                    if is_valid_english_word(ans):
                        break
                    else:
                        print("단어가 존재하지 않습니다.")
                if (len(ans) > self.wordLength):#실제로는 쓰지 않을 조건문
                    continue
                if (False):#사전에 있는지 확인해야함
                    continue

                for i in range(len(ans)):
                        inputWord[turn - 1][i] = ans[i]
                        if (ans[i] == self.keyword[i]):
                            wordStatus[turn - 1][i] = 3
                        else:
                            count = 0
                            for j in range(self.wordLength):
                                #print(ans[i] == keyword[j])
                                if (ans[i] == self.keyword[j]):
                                    wordStatus[turn - 1][i] = 2
                                    count += 1
                            if (count == 0):
                                wordStatus[turn - 1][i] = 1
                break
            
            #출력부
            print("turn :", turn)
            for i in range(self.wordLength + 1):
                if self.checkMatch(inputWord[i], self.keyword, self.wordLength):
                    gameWin = True
                for j in range(self.wordLength):
                    if (wordStatus[i][j] == 0):
                        print("___", end=' ')
                    elif (wordStatus[i][j] == 1):
                        print(' ', inputWord[i][j], ' ',sep='', end=' ')
                    elif(wordStatus[i][j] == 2):
                        print(' ', inputWord[i][j], '?',sep='', end=' ')
                    elif(wordStatus[i][j] == 3):
                        print(' ', inputWord[i][j], '!',sep='', end=' ')
                print()
        
        if (gameWin):
            self.lastTurn = turn
            print("이김")
        elif (gameLose):
            print("짐")#여기 게임결과 반환함수 하나 만들어도 돼? savedata에서 가져가서 점수 할당하고 저장하게네네넨ㄴ

def is_valid_english_word(word):
    translator = Translator()

    try:
        detected_language = translator.detect(word).lang

        if detected_language == 'en':
            translation = translator.translate(word, src=detected_language, dest=detected_language)
            return translation.text.lower() == word.lower()

    except Exception as e:
        print(f"오류 발생: {e}")

    
    return False


