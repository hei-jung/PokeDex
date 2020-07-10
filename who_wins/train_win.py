import numpy as np
import pandas as pd
from sklearn import svm
from train_total import LearnPower
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV


class LearnWinner:
    def __init__(self, pokemon, lang):
        self.path = '../Pokemon/Pokemon_edited.csv'
        self.power = LearnPower('../Pokemon/Pokemon.csv')
        self.lang = lang
        self.X, self.y, self.score = self.power.train_data()
        self.episodes = 800  # 횟수
        self.my = pokemon  # 사용자가 검색한 포켓몬 코드 또는 이름
        self.df = pd.read_csv(self.path)
        self.name = None
        self.type = None
        self.flag = self.checkDigit()

    def checkDigit(self):
        if self.my.isdigit():  # 사용자 입력이 숫자 코드일 경우
            self.my = int(self.my)
            idx = self.X[self.X['Name'] == self.my].index[0]
            if self.lang != 'eng':
                self.name = self.df['Name_' + self.lang][idx]  # 포켓몬의 이름
            else:
                self.name = self.df['Name'][idx]
            self.type = self.df['Type 1'][idx]  # 포켓몬 속성
        else:  # 사용자 입력이 이름일 경우
            self.name = self.my
            try:
                if self.lang != 'eng':
                    idx = self.df[self.df['Name_' + self.lang] == self.name].index[0]
                else:
                    idx = self.df[self.df['Name'] == self.name].index[0]
                self.my = self.X['Name'][idx]
                self.type = self.df['Type 1'][idx]  # 포켓몬 속성
            except IndexError:
                return False
        return True

    def train_winner(self):
        if not self.flag:
            return self.name, '???', 0, 'NOT FOUND'
        # Name열에서 두 개 랜덤으로 뽑아
        name1 = []
        power1 = []
        name2 = []
        power2 = []
        for i in range(self.episodes):
            name1.append(self.my)
            power1.append(self.y[self.X[self.X['Name'] == name1[i]].index[0]])
            name2.append(np.random.randint(1, 800))
            power2.append(self.y[self.X[self.X['Name'] == name2[i]].index[0]])
        X = pd.DataFrame({'name1': name1,
                          'power1': power1,
                          'name2': name2,
                          'power2': power2})
        # print(X)
        y = (X['power1'] > X['power2'])
        # print(y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.14, random_state=95, shuffle=True)
        '''method 1'''
        # clf = svm.SVC(C=1.0, cache_size=200, decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf')   # 정답률 58-74%
        '''method 2'''
        # clf = svm.SVC(C=10, cache_size=200, class_weight='balanced', coef0=0.0,
        #               decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
        #               max_iter=-1, probability=False, random_state=None, shrinking=True,
        #               tol=0.001, verbose=False) # 정답률 46%
        '''method 3'''
        clf = RandomForestClassifier()  # 정답률 93-100%
        '''method 4'''
        # params = [{'C': [1, 10, 100, 1000], 'kernel': ["linear"]},
        #           {'C': [1, 10, 100, 1000], 'kernel': ["rbf"], 'gamma': [0.001, 0.0001]}]
        # clf = GridSearchCV(svm.SVC(), params, n_jobs=1)  # 정답률 100%
        ## 테스트 정답률 계산
        pre = clf.fit(X_train, y_train).predict(X_test)
        # print(X_test)
        # print(y_test)
        # print(pre)
        # pre에서 True면 win.
        pr = (np.count_nonzero(pre == True)) / len(pre)
        # print(pr)
        score = clf.fit(X_train, y_train).score(X_test, y_test)
        win_rate = pr * 100 * (score * self.score)
        print('정확도:', (score * self.score))
        # print('승률:', win_rate, '%')
        if win_rate >= 80:
            if self.lang == 'eng':
                msg = 'Very strong'
            elif self.lang == 'kr':
                msg = '강한 캐릭터입니다.'
            else:
                msg = '強い！！！'
        elif 50 < win_rate < 80:
            if self.lang == 'eng':
                msg = 'Normal'
            elif self.lang == 'kr':
                msg = '보통 캐릭터입니다.'
            else:
                msg = '普通のキャラクターです。'
        else:
            if self.lang == 'eng':
                msg = 'Not suitable for battles'
            elif self.lang == 'kr':
                msg = '공격력이 낮은 캐릭터입니다.'
            else:
                msg = '弱いポケモン'
        return self.name, self.type, win_rate, msg

# pokemon = np.random.randint(1, 800)
# lrn = LearnWinner(pokemon)
# lrn.train_winner()
