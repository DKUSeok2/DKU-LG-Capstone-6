import pandas as pd
import os


def preprocessing(data):

    # '임신 시도 또는 마지막 임신 경과 연수'
    data = data.drop(columns=['임신 시도 또는 마지막 임신 경과 연수']) # 해당 열 삭제(결측치 96%)

    # '특정 시술 유형'
    mode_value = data['특정 시술 유형'].mode()[0]
    data['특정 시술 유형'] = data['특정 시술 유형'].fillna(mode_value) # 최빈값으로 채우기(결측값 2개)

    # '단일 배아 이식 여부'
    data['단일 배아 이식 여부'] = data['단일 배아 이식 여부'].fillna(0) # 0으로 채우기(결측값 6291개)

    # '착상 전 유전 검사 사용 여부'
    data = data.drop(columns=['착상 전 유전 검사 사용 여부']) # 해당 열 삭제(PGS 검사 여부)

    # '착상 전 유전 진단 사용 여부'
    data = data.drop(columns=['착상 전 유전 진단 사용 여부']) # 해당 열 삭제(PGD 검사 여부)

    # '배아 생성 주요 이유' 
    data= data.drop(columns=['배아 생성 주요 이유']) # 해당 열 삭제

    # '총 생성 배아 수'
    data['총 생성 배아 수'] = data['총 생성 배아 수'].fillna(0) # 0으로 채우기(결측값 6291개)
    
    return data


def cover_nan_dahun(df):
    # 대체할 열 목록
    columns_to_fill = [
        '미세주입된 난자 수', '미세주입에서 생성된 배아 수', '이식된 배아 수', 
        '미세주입 배아 이식 수', '저장된 배아 수', '미세주입 후 저장된 배아 수', 
        '해동된 배아 수', '해동 난자 수', '수집된 신선 난자 수', 
        '저장된 신선 난자 수', '혼합된 난자 수'
    ]

    df[columns_to_fill] = df[columns_to_fill].fillna(0)
    
    return df


def preprocess_columns_yooseok(df):
    """
    특정 8개 칼럼에 대한 전처리 수행
    1. '대리모 여부' → 최빈값으로 채우기
    2. 'PGD 시술 여부', 'PGS 시술 여부', '난자 해동 경과일', '배아 해동 경과일' → 삭제
    3. '난자 채취 경과일', '난자 혼합 경과일', '배아 이식 경과일' → 중앙값으로 채우기 (사용한 중앙값 출력)
    
    Parameters:
        data (pd.DataFrame): 입력 데이터프레임
    
    Returns:
        pd.DataFrame: 전처리된 데이터프레임
    """
    
    # 1️⃣ '대리모 여부' → 최빈값으로 결측값 대체
    mode_value = df['대리모 여부'].mode()[0]  # 최빈값 계산
    df['대리모 여부'] = df['대리모 여부'].fillna(mode_value)
    print(f"✅ '대리모 여부' 결측값을 최빈값 ({mode_value}) 으로 대체 완료!")

    # 2️⃣ 'PGD 시술 여부', 'PGS 시술 여부', '난자 해동 경과일', '배아 해동 경과일' → 삭제
    cols_to_drop = ['PGD 시술 여부', 'PGS 시술 여부', '난자 해동 경과일', '배아 해동 경과일']
    df.drop(columns=cols_to_drop, inplace=True, errors='ignore')  # errors='ignore' → 없으면 무시
    print(f"✅ 컬럼 삭제 완료: {cols_to_drop}")

    # 3️⃣ '난자 채취 경과일', '난자 혼합 경과일', '배아 이식 경과일' → 중앙값으로 대체
    cols_for_median = ['난자 채취 경과일', '난자 혼합 경과일', '배아 이식 경과일']
    
    for col in cols_for_median:
        median_value = df[col].median()  # 중앙값 계산
        df[col] = df[col].fillna(median_value)  # NaN을 중앙값으로 대체
        print(f"✅ '{col}' 결측값을 중앙값 ({median_value}) 으로 대체 완료!")

    return df

def cover_nan_hoyeong(df):
    # 1. '난자 출처'의 결측값을 '본인 제공'으로 채우기
    df['난자 출처'].replace('알 수 없음','본인 제공', inplace=True)

    # 2. '난자 기증자 나이' 결측값을 시술 당시 나이로 채우기
    df.loc[df['난자 기증자 나이'] == '알 수 없음', '난자 기증자 나이'] = df['시술 당시 나이']

    # 3. '파트너 정자와 혼합된 난자 수'의 결측값을 0으로 채우기
    df['파트너 정자와 혼합된 난자 수'].fillna(0, inplace=True)

    # 4. '기증자 정자와 혼합된 난자 수'의 결측값을 1로 채우기
    df['기증자 정자와 혼합된 난자 수'].fillna(1, inplace=True)

    # 5. '동결 배아 사용 여부', '신선 배아 사용 여부', '기증 배아 사용 여부'의 결측값을 0으로 채우기
    for column in ['동결 배아 사용 여부', '신선 배아 사용 여부', '기증 배아 사용 여부']:
        df[column].fillna(0, inplace=True)
    
    return df


def missing_value_removal_function(df):
    """
    데이터프레임의 특정 열에 있는 결측치(NaN)를 0으로 대체하는 함수.
    
    파라미터:
        df (pd.DataFrame): NaN을 0으로 대체할 데이터프레임.

    리턴:
        pd.DataFrame: NaN이 0으로 대체된 새로운 데이터프레임.
    """

    # 유진 함수
    df = preprocessing(df)

    # 다훈 함수
    df = cover_nan_dahun(df)

    # 유석 함수
    df = preprocess_columns_yooseok(df)
    # 호영 함수
    df = cover_nan_hoyeong(df)

    return df