# DiffVC Experiment

본 레포지토리는 DiffVC를 쉽게 실험할 수 있도록 원본 코드를 수정한 버전입니다.

코드에 대해 자세히 이해하고 싶으시다면 아래의 paper 및 original repo link를 참고해주세요.

Paper: https://arxiv.org/pdf/2109.13821

Original repo link(official): https://github.com/huawei-noah/Speech-Backbones/tree/main/DiffVC


## 코드 베이스 다운 및 아나콘다 환경 설정

### Clone the repository

```
git clone https://github.com/chaksseu/DiffVC.git
cd DiffVC
```

### 아나콘다 환경 설정 및 필요 패키지 설치

```
conda create -n DiffVC python==3.6.13
conda activate DiffVC
pip install -r requirements.txt
pip install torchaudio
```


## 데이터셋 준비

다음 링크에서 VCTK 데이터를 다운받을 수 있습니다.
https://datashare.ed.ac.uk/handle/10283/2651

데이터셋의 크기가 상당히 크기 때문에 다른 개별적인 데이터를 학습에 이용하셔도 좋습니다. 
(화자와 각 화자의 문장이 많을수록 모델 성능이 올라갑니다.)

1. 'data' directory 생성 
2. 'data' directory 아래에 "wavs", "mels", "embeds" 이름의 폴더 생성
3. 학습 시킬 raw 오디오 파일(.wav)들을 "wavs" 폴더에 삽입
4. get_mels_embeds.py 또는 inference.ipynb 파일을 이용하여 mels, embeds 계산


### 전처리 데이터 저장 위치: 
`'/data/embeds', '/data/mels'`


### 완성된 데이터셋 폴더 구조(예시)
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

Decoder만을 학습시킬 것이기에 vocoder 및 encoder는 사전학습된 모델을 다운받아 사용합니다.

1. 사전 학습된 HiFi-GAN vocoder 다운로드
   - https://drive.google.com/file/d/10khlrM645pTbQ4rc2aNEYPba8RFDBkW-/view?usp=sharing.
   - 위 링크에서 다운 후, checkpts/vocoder/에 넣으시면 됩니다.
2. 사전학습된 인코더 다운로드
   - https://drive.google.com/file/d/1JdoC5hh7k6Nz_oTcumH0nXNEib-GDbSq/view?usp=sharing
   - "logs_enc" directory를 생성하여, 위 링크에서 다운 받은 파일을 넣으시면 됩니다.


## 디코더 학습

`python train_dec.py` 실행

### 학습된 모델 저장 위치: 
`'/logs_dec'`

### 학습/테스트 데이터 에러 그래프 생성/확인 방법: 

1. 'logs_dec'의 train_dec.log파일 값을 복사하여 make_loss_graph.py 파일의 data에 붙여넣기
2. `python make_loss_graph.py`



### 노트북/서버에서 각각의 학습 소요 시간 (200epoch 기준)

```
화자 100명, 화자당 180-350문장의 경우: 노트븍(cpu): X(사실상 불가능), 서버(gpu): 100시간

화자 2명, 화자당 100문장의 경우: 노트븍(cpu): 60시간, 서버(gpu): 40분
```

## 모델 테스트 (오디오 생성)

`inference.ipynb` 및 `_inference.py` 참고
```
# 학습시킨 모델을 사용하여 Vocie Conversion을 진행

(경로 설정 예시)
vc_path = 'logs_dec/vc_200.pt' (학습시킨 모델 경로)
src_path = 'data/p226/p226_005_mic1.wav' (source wav 파일 경로)
tgt_path = 'data/p229/p229_002_mic1.wav' (target wav 파일 경로)
output_path = 'converted_audio/converted.wav' (변환된 음성이 저장될 경로)
```

### 결과 저장 위치: 
`'converted_audio/converted.wav'`

### MCD 확인 방법: 
- 아래 방법을 따라 `cal_pymcd.py` 실행
- gt_wav: target 화자가 source의 문장을 말한 wav파일
- ex) A화자의 1번 문장을 Source로 B화자의 2번문장을 Target으로 Voice Conversion을 진행한 경우, B화자의 1번 문장이 gt_wav가 되며, 모델을 통해 변환한 음성이 converted_wav가 됩니다.
- gt_wav와 converted_wav의 mcd값을 측정
```
# 새로운 conda 환경 생성 및 python 파일 실행
conda create -n mcd python==3.8
conda activate mcd
pip install pymcd tqdm
# 'cal_pymcd.py'에서 GT path와 Converted path 설정 후
python cal_pymcd.py
```

### 결과 파일 재생 방법: 
`'/converted_audio'`에서 원하는 wav파일을 다운받아 재생