from pymcd.mcd import Calculate_MCD
import os
import json
import argparse
import numpy as np
from tqdm import tqdm
import pprint


# gt_wav=f'data/{speaker}/{gt_wav}' 
# converted_wav='converted_audio/converted.wav'
# A화자의 1번 문장을 Source로 B화자의 2번문장을 Target으로 Voice Conversion을 진행한 경우
# B화자의 1번 문장(원본)이 gt_wav가 되며, 모델을 통해 변환한 음성이 converted_wav가 됩니다.

gt_wav='' 
converted_wav=''

def calculate_mcd(gt_wav, converted_wav, mcd_mode='dtw'):
    mcd_toolbox = Calculate_MCD(MCD_mode=mcd_mode)
    mcd_result = mcd_toolbox.calculate_mcd(gt_wav, converted_wav)
    print(mcd_result)

calculate_mcd(gt_wav, converted_wav)