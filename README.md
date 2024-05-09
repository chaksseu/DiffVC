# DiffVC Experiment

본 레포지토리는 아래 링크의 original code를 쉽게 실험할 수 있도록 수정한 버전입니다.

코드에 대해 자세히 이해하고 싶으시다면 paper와 original repo link를 참고해주세요.

Paper: https://arxiv.org/pdf/2109.13821

Original repo link(non-official): https://github.com/huawei-noah/Speech-Backbones/tree/main/DiffVC


## 코드 베이스 다운 및 아나콘다 환경 설정

Clone the repository

```
git clone https://github.com/chaksseu/DiffVC.git
cd DiffVC
```

아나콘다 환경 설정 및 필요 패키지 설치

```
conda create -n DiffVC python==3.6.13
conda activate DiffVC
pip install -r requirements.txt
```


## 데이터셋 준비

아래 링크에서 VCTK 데이터를 다운받을 수 있습니다.
https://datashare.ed.ac.uk/handle/10283/2651

데이터셋의 크기가 상당히 크기 때문에 다른 개별적인 데이터를 학습에 이용하셔도 좋습니다. (화자와 문장의 수가 많을수록 모델 성능이 올라갑니다.)

1. 'data' directory 생성 및 train_dec.py의 data_dir을 '../data'로 변경
2. 'data' directory 아래에 "wavs", "mels", "embeds" 이름의 폴더 생성
3. 학습 시킬 raw 오디오 파일들을 "wavs" 폴더에 삽입 (wav파일은 22050으로 다운 샘플링 필요)
4. get_mels_embeds.py 또는 inference.ipynb 파일을 이용하여 mels, embeds 계산

완성된 데이터셋 폴더 구조(예시)
```
│ ├─data
│ │ ├─embeds
│ │ │ ├─p229
│ │ │ └─p238
│ │ ├─mels
│ │ │ ├─p229
│ │ │ └─p238
│ │ └─wavs
│ │ ├─p229
│ │ └─p238
```

## 사전 학습모델 다운로드

1. 사전 학습된 HiFi-GAN vocoder 다운로드
   - https://drive.google.com/file/d/10khlrM645pTbQ4rc2aNEYPba8RFDBkW-/view?usp=sharing.
   
   - 위 링크에서 다운 후, checkpts/vocoder/에 넣으시면 됩니다.
2. 사전학습된 인코더 다운로드
   - https://drive.google.com/file/d/1JdoC5hh7k6Nz_oTcumH0nXNEib-GDbSq/view?usp=sharing
   - "logs_enc" directory를 생성하여, 위 링크에서 다운 받은 파일을 넣으시면 됩니다.


## 디코더 학습

train_dec.py 파일 실행


## 모델 테스트 (오디오 생성)

inference.ipynb 파일을 통해, 학습시킨 모델을 이용하여 변환된 음성을 얻을 수 있습니다. 