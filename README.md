# DKU-LG-Capstone-6

## 2월 부터 해커톤 시작

## 결측치 제거한 훈련 데이터 로드하는 방법
```
import sys
import os
import pandas as pd

# 현재 작업 디렉토리 경로를 가져와 shared codes 폴더의 위치를 sys.path에 추가합니다.
# sys.path에 추가된 경로에 있는 py 폴더는 임포트할 수 있다.
current_dir = os.getcwd()
shared_codes_dir = os.path.join(current_dir, '../shared codes')
sys.path.append(shared_codes_dir)


# cover_nan 모듈을 임포트
from cover_nan import missing_value_removal_function

# 원본 train 데이터 로드
train = pd.read_csv("../shared codes/data/train.csv")
test = pd.read_csv("../shared codes/data/test.csv")

# missing_value_removal_function 사용
train = missing_value_removal_function(train)
test = missing_value_removal_function(test)
```