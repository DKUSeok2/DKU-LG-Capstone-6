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

# missing_value_removal_function 사용
df = missing_value_removal_function(train)
```

## IVF vs DI 분리한 데이터 로드하는 방법
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
from cover_nan_0224_IVFDI import missing_value_removal_function

# 원본 train 데이터 로드
train = pd.read_csv("../shared codes/data/train.csv")
test = pd.read_csv("../shared codes/data/test.csv")

# missing_value_removal_function 사용
train_IVF, train_DI = missing_value_removal_function(train)
test_IVF, test_DI = missing_value_removal_function(test)
```

## 난자 나이 기준으로 분리한 데이터 로드하는 방법
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
from cover_nan_0215_dahun import missing_value_removal_function

# 원본 train 데이터 로드
train = pd.read_csv("../shared codes/data/train.csv")
test = pd.read_csv("../shared codes/data/test.csv")

# missing_value_removal_function 사용
train_young, train_middle, train_old, train_unknown = missing_value_removal_function(train)
test_young, test_middle, test_old, test_unknown = missing_value_removal_function(test)
```

## 난자 나이, IVF/DI, 배아 생성 주요 이유를 기준으로 분리한 데이터 로드하는 방법
```import sys
import os
import pandas as pd

# 현재 작업 디렉토리 경로를 가져와 shared codes 폴더의 위치를 sys.path에 추가합니다.
# sys.path에 추가된 경로에 있는 py 폴더는 임포트할 수 있다.
current_dir = os.getcwd()
shared_codes_dir = os.path.join(current_dir, '../shared codes')
sys.path.append(shared_codes_dir)


# cover_nan 모듈을 임포트
from cover_nan_0224_age_IVFDI import missing_value_removal_function

# 원본 train 데이터 로드
train = pd.read_csv("../shared codes/data/train.csv")
test = pd.read_csv("../shared codes/data/test.csv")

# missing_value_removal_function 사용
train_young_IVF, train_young_DI, train_middle_IVF, train_middle_DI, train_old_IVF, train_old_DI, train_unknown, train_0 = missing_value_removal_function(train)
test_young_IVF, test_young_DI, test_middle_IVF, test_middle_DI, test_old_IVF, test_old_DI, test_unknown, test_0 = missing_value_removal_function(test)
```