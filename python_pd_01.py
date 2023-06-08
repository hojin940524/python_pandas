# -*- coding: utf-8 -*-

# 예제 1-1 딕셔너리 -> 시리즈 변환

import pandas as pd #판다스 불러오기
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
sr = pd.Series(dict_data)

print(sr)

# 예제 1-2 시리즈 인덱스
list_data = ['2023-06-08', 3.14, 'HOJIN', 100, True]
sr_1 = pd.Series(list_data)
print(sr_1)  #시리즈 - 정수형 위치 인덱스가 자동으로 설정된다.

idx = sr_1.index     # .index -> 인덱스 배열을 불러옴.
val = sr_1.values    # .values -> 데이터 값의 배열을 불러옴.
print(idx) 
print(val)

# 예제 1-3 시리즈 원소 선택
tup_data = ('호진', '1994-05-24', '여', True)
sr_2 = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr_2)

print(sr_2[0])
print(sr_2['이름'])
print(sr_2[[1,2]])
print(sr_2[['생년월일', '성별']])
print(sr_2[1:2])  #범위 지정(정수형일 경우) - 끝 포함 X
print(sr_2['생년월일':'학생여부']) #범위 지정(인덱스 이름 사용) - 끝 포함

# 예제 1-4 딕셔너리 -> 데이터프레임 변환
dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}
df = pd.DataFrame(dict_data)
print(df)

# 예제 1-5 행 인덱스/열 이름 설정
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns = ['나이', '성별', '학교'])
print(df)
print(df.index)
print(df.columns)

df.index = ['학생1', '학생2']
df.columns = ['연령', '나이', '소속']
print(df)

# 예제 1-6 행 인덱스/열 이름 변경
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns = ['나이', '성별', '학교'])
print(df)
df.rename(columns = {'나이':'연령', '성별':'남녀','학교':'소속'}, inplace = True)
df.rename(index = {'준서':'학생1', '예은':'학생2'}, inplace = True)
print(df)


# 예제 1-7 행 삭제 => axis = 0 혹은 생략
exam_data = {'수학' : [90,80,70], '영어' : [98,89,95], '음악' : [85,95,100], '체육' : [100,90,90]}
df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
print(df)

df.drop('우현', inplace = True)
print(df)
df.drop(['인아', '서준'], axis = 0, inplace = True)
print(df)

# 예제 1-8 열 삭제 => axis = 1
exam_data = {'수학' : [90,80,70], '영어' : [98,89,95], '음악' : [85,95,100], '체육' : [100,90,90]}
df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])

df1 =df.copy()
df1.drop('수학', axis = 1, inplace=True)
print(df1)
df2 = df.copy()
df2.drop(['영어', '음악'], axis = 1, inplace = True)
print(df2)

# 예제 1-9 행 선택
exam_data = {'수학' : [90,80,70], '영어' : [98,89,95], '음악' : [85,95,100], '체육' : [100,90,90]}
df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])

label1 = df.loc['서준'] # .loc => 인덱스 이름 직접 입력
position1 = df.iloc[0] # .iloc => 정수형 위치 입력
print(label1)
print(position1)

label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0,1]]
print(label2)
print(position2)

label3 = df.loc['서준':'우현'] # 인덱스 이름 직접 입력시, 우현 포함
position3 = df.iloc[0:1] #정수형으로 입력시, 우현 불포함
print(label3)
print(position3)

# 예제 1-10 열 선택
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90,80,70], '영어' : [98,89,95], '음악' : [85,95,100], '체육' : [100,90,90],}
df = pd.DataFrame(exam_data)
print(df)

math1 = df['수학']
print(math1)

eng = df.영어
print(eng)

music_gym = df[['음악', '체육']]
print(music_gym)

math2 = df[['수학']]
print(math2)
