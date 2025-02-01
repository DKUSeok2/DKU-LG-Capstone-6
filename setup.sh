#!/bin/bash

# 새로운 conda 환경 생성 (aimers 이름, python 3.12.2 버전)
conda create -n aimers python=3.12.2 -y

# 생성된 환경 활성화
conda activate aimers

# 필요한 패키지들 설치
conda install -y scikit-learn=1.6.1 numpy=2.2.2 pandas=2.2.3 matplotlib=3.10.0 seaborn=0.13.2

# conda가 패키지를 찾지 못할 경우 pip로 설치
pip install scikit-learn==1.6.1 numpy==2.2.2 pandas==2.2.3 matplotlib==3.10.0 seaborn==0.13.2

echo "Environment setup complete!"