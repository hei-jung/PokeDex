import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV


class LearnPower:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(self.path)  # 파일 읽어들이기

    def train_data(self):
        ## 학습 데이터
        del self.df['Type 1'], self.df['Type 2']
        self.df['Name'] = pd.Categorical(self.df['Name'])
        self.df['Name'] = self.df['Name'].cat.codes
        X = self.df.drop('Total', 1)
        ## 레이블
        y = []
        m = max(self.df.Total)  # Total 컬럼의 최댓값
        for t in self.df['Total']:
            y.append(int(round((t / m), 1) * 10) - 1)  # Total값 그대로 넣으면 숫자 종류가 너무 많아서 학습능률이 떨어진다.
            ## 해결방법
            # (1) 최댓값으로 나눈 것을 소숫점 첫째자리까지 반올림한다. (ex.0.6)
            # (2) 소수는 학습 잘 못한다. 연속적인 숫자라서 값을 예측하기 힘든 듯. -> 10을 곱해서 정수로 만든다.
            # (3) 1을 뺀다. (=> 정답 값의 범위: 1~8이 됨.)
        # print(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.14, random_state=95, shuffle=True)
        '''method 1'''
        # clf = svm.SVC(C=1.0, cache_size=200, decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf')   # 정답률 30%
        '''method 2'''
        # clf = svm.SVC(C=10, cache_size=200, class_weight='balanced', coef0=0.0,
        #               decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
        #               max_iter=-1, probability=False, random_state=None, shrinking=True,
        #               tol=0.001, verbose=False) # 정답률 30%
        '''method 3'''
        # clf = RandomForestClassifier()  # 정답률 70%
        '''method 4'''
        params = [{'C': [1, 10, 100, 1000], 'kernel': ["linear"]},
                  {'C': [1, 10, 100, 1000], 'kernel': ["rbf"], 'gamma': [0.001, 0.0001]}]
        clf = GridSearchCV(svm.SVC(), params, n_jobs=1)  # 정답률 97%
        # 테스트 정답률 계산
        pre = clf.fit(X_train, y_train).predict(X_test)
        # print('pre:')
        # print(pre)
        score = clf.fit(X_train, y_train).score(X_test, y_test)
        # print('정답률:', score)
        return X, y, score

# lrn = LearnPower()
# lrn.train_data()
