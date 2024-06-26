import matplotlib.pyplot as plt
import numpy as np

# logs_dec/train_dec.log파일의 값을 아래 data에 대신 넣으시면 됩니다.

data = """
Epoch 1: loss = 0.1779
Epoch 2: loss = 0.1237
Epoch 3: loss = 0.1198
Epoch 4: loss = 0.1165
Epoch 5: loss = 0.1158
Epoch 6: loss = 0.1162
Epoch 7: loss = 0.1158
Epoch 8: loss = 0.1129
Epoch 9: loss = 0.1115
Epoch 10: loss = 0.1124
Epoch 11: loss = 0.1107
Epoch 12: loss = 0.1116
Epoch 13: loss = 0.1095
Epoch 14: loss = 0.1079
Epoch 15: loss = 0.1108
Epoch 16: loss = 0.1060
Epoch 17: loss = 0.1081
Epoch 18: loss = 0.1066
Epoch 19: loss = 0.1087
Epoch 20: loss = 0.1057
Epoch 21: loss = 0.1062
Epoch 22: loss = 0.1070
Epoch 23: loss = 0.1078
Epoch 24: loss = 0.1064
Epoch 25: loss = 0.1063
Epoch 26: loss = 0.1066
Epoch 27: loss = 0.1068
Epoch 28: loss = 0.1058
Epoch 29: loss = 0.1052
Epoch 30: loss = 0.1057
Epoch 31: loss = 0.1057
Epoch 32: loss = 0.1055
Epoch 33: loss = 0.1046
Epoch 34: loss = 0.1046
Epoch 35: loss = 0.1052
Epoch 36: loss = 0.1046
Epoch 37: loss = 0.1053
Epoch 38: loss = 0.1049
Epoch 39: loss = 0.1034
Epoch 40: loss = 0.1037
Epoch 41: loss = 0.1051
Epoch 42: loss = 0.1039
Epoch 43: loss = 0.1033
Epoch 44: loss = 0.1058
Epoch 45: loss = 0.1039
Epoch 46: loss = 0.1025
Epoch 47: loss = 0.1031
Epoch 48: loss = 0.1037
Epoch 49: loss = 0.1034
Epoch 50: loss = 0.1046
Epoch 51: loss = 0.1037
Epoch 52: loss = 0.1044
Epoch 53: loss = 0.1029
Epoch 54: loss = 0.1022
Epoch 55: loss = 0.1026
Epoch 56: loss = 0.1031
Epoch 57: loss = 0.1031
Epoch 58: loss = 0.1030
Epoch 59: loss = 0.1036
Epoch 60: loss = 0.1025
Epoch 61: loss = 0.1031
Epoch 62: loss = 0.1042
Epoch 63: loss = 0.1038
Epoch 64: loss = 0.1034
Epoch 65: loss = 0.1031
Epoch 66: loss = 0.1023
Epoch 67: loss = 0.1029
Epoch 68: loss = 0.1018
Epoch 69: loss = 0.1007
Epoch 70: loss = 0.1022
Epoch 71: loss = 0.1020
Epoch 72: loss = 0.1026
Epoch 73: loss = 0.1008
Epoch 74: loss = 0.1024
Epoch 75: loss = 0.1012
Epoch 76: loss = 0.1016
Epoch 77: loss = 0.1036
Epoch 78: loss = 0.1018
Epoch 79: loss = 0.1009
Epoch 80: loss = 0.1009
Epoch 81: loss = 0.1011
Epoch 82: loss = 0.1012
Epoch 83: loss = 0.1024
Epoch 84: loss = 0.1025
Epoch 85: loss = 0.1015
Epoch 86: loss = 0.0998
Epoch 87: loss = 0.1011
Epoch 88: loss = 0.1033
Epoch 89: loss = 0.1024
Epoch 90: loss = 0.1032
Epoch 91: loss = 0.1033
Epoch 92: loss = 0.1014
Epoch 93: loss = 0.1008
Epoch 94: loss = 0.1011
Epoch 95: loss = 0.1010
Epoch 96: loss = 0.1001
Epoch 97: loss = 0.1001
Epoch 98: loss = 0.1011
Epoch 99: loss = 0.1024
Epoch 100: loss = 0.1007
Epoch 101: loss = 0.0998
Epoch 102: loss = 0.1010
Epoch 103: loss = 0.1004
Epoch 104: loss = 0.1014
Epoch 105: loss = 0.1002
Epoch 106: loss = 0.1003
Epoch 107: loss = 0.0998
Epoch 108: loss = 0.0996
Epoch 109: loss = 0.0994
Epoch 110: loss = 0.0997
Epoch 111: loss = 0.1007
Epoch 112: loss = 0.0990
Epoch 113: loss = 0.0997
Epoch 114: loss = 0.0994
Epoch 115: loss = 0.1003
Epoch 116: loss = 0.1011
Epoch 117: loss = 0.1009
Epoch 118: loss = 0.0991
Epoch 119: loss = 0.0992
Epoch 120: loss = 0.0998
Epoch 121: loss = 0.1002
Epoch 122: loss = 0.1007
Epoch 123: loss = 0.1004
Epoch 124: loss = 0.0995
Epoch 125: loss = 0.1004
Epoch 126: loss = 0.0998
Epoch 127: loss = 0.0994
Epoch 128: loss = 0.1007
Epoch 129: loss = 0.0991
Epoch 130: loss = 0.1009
Epoch 131: loss = 0.0994
Epoch 132: loss = 0.0990
Epoch 133: loss = 0.1015
Epoch 134: loss = 0.0986
Epoch 135: loss = 0.1002
Epoch 136: loss = 0.1000
Epoch 137: loss = 0.0996
Epoch 138: loss = 0.0994
Epoch 139: loss = 0.0988
Epoch 140: loss = 0.0996
Epoch 141: loss = 0.0989
Epoch 142: loss = 0.0991
Epoch 143: loss = 0.1002
Epoch 144: loss = 0.0985
Epoch 145: loss = 0.1004
Epoch 146: loss = 0.0998
Epoch 147: loss = 0.0981
Epoch 148: loss = 0.0989
Epoch 149: loss = 0.0997
Epoch 150: loss = 0.0993
Epoch 151: loss = 0.0984
Epoch 152: loss = 0.0993
Epoch 153: loss = 0.0993
Epoch 154: loss = 0.1006
Epoch 155: loss = 0.1009
Epoch 156: loss = 0.0989
Epoch 157: loss = 0.0974
Epoch 158: loss = 0.0978
Epoch 159: loss = 0.0988
Epoch 160: loss = 0.0984
Epoch 161: loss = 0.0985
Epoch 162: loss = 0.1005
Epoch 163: loss = 0.0987
Epoch 164: loss = 0.0992
Epoch 165: loss = 0.0987
Epoch 166: loss = 0.1003
Epoch 167: loss = 0.1000
Epoch 168: loss = 0.0983
Epoch 169: loss = 0.0988
Epoch 170: loss = 0.1004
Epoch 171: loss = 0.0991
Epoch 172: loss = 0.0985
Epoch 173: loss = 0.0999
Epoch 174: loss = 0.1012
Epoch 175: loss = 0.0993
Epoch 176: loss = 0.0980
Epoch 177: loss = 0.0987
Epoch 178: loss = 0.0991
Epoch 179: loss = 0.0987
Epoch 180: loss = 0.0986
Epoch 181: loss = 0.0985
Epoch 182: loss = 0.0968
Epoch 183: loss = 0.0993
Epoch 184: loss = 0.0973
Epoch 185: loss = 0.0981
Epoch 186: loss = 0.0993
Epoch 187: loss = 0.0974
Epoch 188: loss = 0.0989
Epoch 189: loss = 0.0974
Epoch 190: loss = 0.0985
Epoch 191: loss = 0.0989
Epoch 192: loss = 0.0992
Epoch 193: loss = 0.0973
Epoch 194: loss = 0.0980
Epoch 195: loss = 0.0975
Epoch 196: loss = 0.0990
Epoch 197: loss = 0.0969
Epoch 198: loss = 0.0973
Epoch 199: loss = 0.0981
Epoch 200: loss = 0.0978
"""

# 각 줄을 분할하여 필요한 값을 추출하고 리스트에 저장
loss_list = [float(line.split(",")[0].split("=")[1]) for line in data.split("\n") if line.strip()]
#cyc_loss_list = [float(line.split(",")[1].split("=")[1]) for line in data.split("\n") if line.strip()]
#total_loss_list = [float(line.split(",")[2].split("=")[1]) for line in data.split("\n") if line.strip()]

# Epoch 번호 (1부터 시작)
epochs = range(1, len(loss_list) + 1)


# y축 범위 설정
#plt.ylim(0.0, 0.3)
# y축 틱 설정
#plt.yticks(np.arange(0.0, 0.3, 0.1))


# Loss 그래프
plt.plot(epochs, loss_list, label='Loss', color='blue')
# Cycle Loss 그래프
#plt.plot(epochs, cyc_loss_list, label='Cycle Loss', color='red')
# Total Loss 그래프
#plt.plot(epochs, total_loss_list, label='Total Loss', color='green')

plt.title('Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()
# 이미지로 저장
plt.savefig('loss_graph.png')
