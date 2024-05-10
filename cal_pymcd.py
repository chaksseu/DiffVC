from pymcd.mcd import Calculate_MCD
import os
import json
import argparse
import numpy as np
from tqdm import tqdm
import pprint


# gt_wav=f'data/{speaker}/{gt_wav}' 
# converted_wav='converted_audio/{vc_path}/{src_path}_to_{tgt_path}.wav'

gt_wav='' 
converted_wav=''

def calculate_mcd(gt_wav, converted_wav, mcd_mode='dtw'):
    mcd_toolbox = Calculate_MCD(MCD_mode=mcd_mode)
    mcd_result = mcd_toolbox.calculate_mcd(gt_wav, converted_wav)
    print(mcd_result)

calculate_mcd(gt_wav, converted_wav)