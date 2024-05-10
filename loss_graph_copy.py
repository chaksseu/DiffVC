import matplotlib.pyplot as plt
import numpy as np

data = """
Epoch 1: loss = 0.1501, cyc_loss = 0.0891, total_loss = 0.2391
Epoch 2: loss = 0.1246, cyc_loss = 0.0412, total_loss = 0.1658
Epoch 3: loss = 0.1217, cyc_loss = 0.0388, total_loss = 0.1605
Epoch 4: loss = 0.1186, cyc_loss = 0.0360, total_loss = 0.1546
Epoch 5: loss = 0.1195, cyc_loss = 0.0348, total_loss = 0.1542
Epoch 6: loss = 0.1170, cyc_loss = 0.0334, total_loss = 0.1504
Epoch 7: loss = 0.1151, cyc_loss = 0.0329, total_loss = 0.1480
Epoch 8: loss = 0.1153, cyc_loss = 0.0316, total_loss = 0.1469
Epoch 9: loss = 0.1156, cyc_loss = 0.0318, total_loss = 0.1474
Epoch 10: loss = 0.1137, cyc_loss = 0.0308, total_loss = 0.1446
Epoch 11: loss = 0.1134, cyc_loss = 0.0301, total_loss = 0.1435
Epoch 12: loss = 0.1139, cyc_loss = 0.0283, total_loss = 0.1422
Epoch 13: loss = 0.1115, cyc_loss = 0.0288, total_loss = 0.1404
Epoch 14: loss = 0.1117, cyc_loss = 0.0286, total_loss = 0.1404
Epoch 15: loss = 0.1116, cyc_loss = 0.0280, total_loss = 0.1396
Epoch 16: loss = 0.1104, cyc_loss = 0.0274, total_loss = 0.1378
Epoch 17: loss = 0.1108, cyc_loss = 0.0270, total_loss = 0.1378
Epoch 18: loss = 0.1099, cyc_loss = 0.0265, total_loss = 0.1363
Epoch 19: loss = 0.1097, cyc_loss = 0.0264, total_loss = 0.1361
Epoch 20: loss = 0.1106, cyc_loss = 0.0261, total_loss = 0.1367
Epoch 21: loss = 0.1097, cyc_loss = 0.0264, total_loss = 0.1361
Epoch 22: loss = 0.1112, cyc_loss = 0.0249, total_loss = 0.1361
Epoch 23: loss = 0.1117, cyc_loss = 0.0258, total_loss = 0.1375
Epoch 24: loss = 0.1105, cyc_loss = 0.0254, total_loss = 0.1358
Epoch 25: loss = 0.1103, cyc_loss = 0.0248, total_loss = 0.1351
Epoch 26: loss = 0.1106, cyc_loss = 0.0243, total_loss = 0.1349
Epoch 27: loss = 0.1111, cyc_loss = 0.0250, total_loss = 0.1361
Epoch 28: loss = 0.1100, cyc_loss = 0.0245, total_loss = 0.1344
Epoch 29: loss = 0.1103, cyc_loss = 0.0237, total_loss = 0.1340
Epoch 30: loss = 0.1103, cyc_loss = 0.0241, total_loss = 0.1345
Epoch 31: loss = 0.1090, cyc_loss = 0.0240, total_loss = 0.1330
Epoch 32: loss = 0.1097, cyc_loss = 0.0238, total_loss = 0.1335
Epoch 33: loss = 0.1101, cyc_loss = 0.0233, total_loss = 0.1335
Epoch 34: loss = 0.1102, cyc_loss = 0.0231, total_loss = 0.1332
Epoch 35: loss = 0.1091, cyc_loss = 0.0231, total_loss = 0.1322
Epoch 36: loss = 0.1089, cyc_loss = 0.0231, total_loss = 0.1320
Epoch 37: loss = 0.1090, cyc_loss = 0.0228, total_loss = 0.1318
Epoch 38: loss = 0.1081, cyc_loss = 0.0226, total_loss = 0.1308
Epoch 39: loss = 0.1093, cyc_loss = 0.0225, total_loss = 0.1318
Epoch 40: loss = 0.1093, cyc_loss = 0.0219, total_loss = 0.1312
Epoch 41: loss = 0.1087, cyc_loss = 0.0220, total_loss = 0.1307
Epoch 42: loss = 0.1080, cyc_loss = 0.0218, total_loss = 0.1298
Epoch 43: loss = 0.1079, cyc_loss = 0.0213, total_loss = 0.1292
Epoch 44: loss = 0.1066, cyc_loss = 0.0214, total_loss = 0.1280
Epoch 45: loss = 0.1085, cyc_loss = 0.0214, total_loss = 0.1298
Epoch 46: loss = 0.1059, cyc_loss = 0.0207, total_loss = 0.1266
Epoch 47: loss = 0.1081, cyc_loss = 0.0211, total_loss = 0.1292
Epoch 48: loss = 0.1086, cyc_loss = 0.0217, total_loss = 0.1303
Epoch 49: loss = 0.1074, cyc_loss = 0.0207, total_loss = 0.1281
Epoch 50: loss = 0.1088, cyc_loss = 0.0210, total_loss = 0.1298
Epoch 51: loss = 0.1077, cyc_loss = 0.0205, total_loss = 0.1281
Epoch 52: loss = 0.1069, cyc_loss = 0.0205, total_loss = 0.1273
Epoch 53: loss = 0.1061, cyc_loss = 0.0208, total_loss = 0.1269
Epoch 54: loss = 0.1089, cyc_loss = 0.0206, total_loss = 0.1295
Epoch 55: loss = 0.1082, cyc_loss = 0.0201, total_loss = 0.1283
Epoch 56: loss = 0.1057, cyc_loss = 0.0195, total_loss = 0.1252
Epoch 57: loss = 0.1073, cyc_loss = 0.0201, total_loss = 0.1274
Epoch 58: loss = 0.1089, cyc_loss = 0.0195, total_loss = 0.1284
Epoch 59: loss = 0.1068, cyc_loss = 0.0196, total_loss = 0.1264
Epoch 60: loss = 0.1049, cyc_loss = 0.0197, total_loss = 0.1245
Epoch 61: loss = 0.1077, cyc_loss = 0.0197, total_loss = 0.1273
Epoch 62: loss = 0.1063, cyc_loss = 0.0196, total_loss = 0.1259
Epoch 63: loss = 0.1080, cyc_loss = 0.0193, total_loss = 0.1273
Epoch 64: loss = 0.1066, cyc_loss = 0.0189, total_loss = 0.1255
Epoch 65: loss = 0.1070, cyc_loss = 0.0191, total_loss = 0.1261
Epoch 66: loss = 0.1077, cyc_loss = 0.0186, total_loss = 0.1263
Epoch 67: loss = 0.1077, cyc_loss = 0.0188, total_loss = 0.1264
Epoch 68: loss = 0.1058, cyc_loss = 0.0174, total_loss = 0.1231
Epoch 69: loss = 0.1056, cyc_loss = 0.0180, total_loss = 0.1236
Epoch 70: loss = 0.1079, cyc_loss = 0.0181, total_loss = 0.1260
Epoch 71: loss = 0.1065, cyc_loss = 0.0181, total_loss = 0.1246
Epoch 72: loss = 0.1059, cyc_loss = 0.0179, total_loss = 0.1238
Epoch 73: loss = 0.1075, cyc_loss = 0.0176, total_loss = 0.1251
Epoch 74: loss = 0.1072, cyc_loss = 0.0178, total_loss = 0.1250
Epoch 75: loss = 0.1062, cyc_loss = 0.0177, total_loss = 0.1240
Epoch 76: loss = 0.1072, cyc_loss = 0.0170, total_loss = 0.1242
Epoch 77: loss = 0.1071, cyc_loss = 0.0173, total_loss = 0.1245
Epoch 78: loss = 0.1060, cyc_loss = 0.0176, total_loss = 0.1236
Epoch 79: loss = 0.1069, cyc_loss = 0.0171, total_loss = 0.1240
Epoch 80: loss = 0.1067, cyc_loss = 0.0174, total_loss = 0.1241
Epoch 81: loss = 0.1056, cyc_loss = 0.0170, total_loss = 0.1227
Epoch 82: loss = 0.1066, cyc_loss = 0.0170, total_loss = 0.1236
Epoch 83: loss = 0.1070, cyc_loss = 0.0172, total_loss = 0.1242
Epoch 84: loss = 0.1073, cyc_loss = 0.0169, total_loss = 0.1242
Epoch 85: loss = 0.1053, cyc_loss = 0.0168, total_loss = 0.1221
Epoch 86: loss = 0.1057, cyc_loss = 0.0166, total_loss = 0.1223
Epoch 87: loss = 0.1052, cyc_loss = 0.0163, total_loss = 0.1215
Epoch 88: loss = 0.1063, cyc_loss = 0.0159, total_loss = 0.1223
Epoch 89: loss = 0.1051, cyc_loss = 0.0161, total_loss = 0.1213
Epoch 90: loss = 0.1055, cyc_loss = 0.0159, total_loss = 0.1214
Epoch 91: loss = 0.1067, cyc_loss = 0.0156, total_loss = 0.1223
Epoch 92: loss = 0.1069, cyc_loss = 0.0162, total_loss = 0.1230
Epoch 93: loss = 0.1044, cyc_loss = 0.0159, total_loss = 0.1203
Epoch 94: loss = 0.1063, cyc_loss = 0.0154, total_loss = 0.1217
Epoch 95: loss = 0.1058, cyc_loss = 0.0156, total_loss = 0.1214
Epoch 96: loss = 0.1068, cyc_loss = 0.0153, total_loss = 0.1221
Epoch 97: loss = 0.1060, cyc_loss = 0.0155, total_loss = 0.1216
Epoch 98: loss = 0.1059, cyc_loss = 0.0153, total_loss = 0.1212
Epoch 99: loss = 0.1054, cyc_loss = 0.0144, total_loss = 0.1198
Epoch 100: loss = 0.1046, cyc_loss = 0.0152, total_loss = 0.1198
Epoch 101: loss = 0.1054, cyc_loss = 0.0153, total_loss = 0.1206
Epoch 102: loss = 0.1054, cyc_loss = 0.0151, total_loss = 0.1204
Epoch 103: loss = 0.1049, cyc_loss = 0.0146, total_loss = 0.1195
Epoch 104: loss = 0.1059, cyc_loss = 0.0149, total_loss = 0.1208
Epoch 105: loss = 0.1050, cyc_loss = 0.0147, total_loss = 0.1197
Epoch 106: loss = 0.1030, cyc_loss = 0.0149, total_loss = 0.1180
Epoch 107: loss = 0.1059, cyc_loss = 0.0146, total_loss = 0.1204
Epoch 108: loss = 0.1054, cyc_loss = 0.0143, total_loss = 0.1198
Epoch 109: loss = 0.1057, cyc_loss = 0.0143, total_loss = 0.1200
Epoch 110: loss = 0.1045, cyc_loss = 0.0143, total_loss = 0.1188
Epoch 111: loss = 0.1054, cyc_loss = 0.0141, total_loss = 0.1195
Epoch 112: loss = 0.1059, cyc_loss = 0.0146, total_loss = 0.1205
Epoch 113: loss = 0.1046, cyc_loss = 0.0140, total_loss = 0.1186
Epoch 114: loss = 0.1048, cyc_loss = 0.0142, total_loss = 0.1190
Epoch 115: loss = 0.1053, cyc_loss = 0.0139, total_loss = 0.1191
Epoch 116: loss = 0.1056, cyc_loss = 0.0144, total_loss = 0.1200
Epoch 117: loss = 0.1057, cyc_loss = 0.0144, total_loss = 0.1201
Epoch 118: loss = 0.1062, cyc_loss = 0.0149, total_loss = 0.1210
Epoch 119: loss = 0.1075, cyc_loss = 0.0138, total_loss = 0.1214
Epoch 120: loss = 0.1056, cyc_loss = 0.0145, total_loss = 0.1201
Epoch 121: loss = 0.1045, cyc_loss = 0.0139, total_loss = 0.1184
Epoch 122: loss = 0.1042, cyc_loss = 0.0136, total_loss = 0.1178
Epoch 123: loss = 0.1065, cyc_loss = 0.0135, total_loss = 0.1201
Epoch 124: loss = 0.1046, cyc_loss = 0.0139, total_loss = 0.1186
Epoch 125: loss = 0.1038, cyc_loss = 0.0137, total_loss = 0.1175
Epoch 126: loss = 0.1046, cyc_loss = 0.0139, total_loss = 0.1184
Epoch 127: loss = 0.1043, cyc_loss = 0.0137, total_loss = 0.1181
Epoch 128: loss = 0.1043, cyc_loss = 0.0135, total_loss = 0.1178
Epoch 129: loss = 0.1040, cyc_loss = 0.0137, total_loss = 0.1177
Epoch 130: loss = 0.1029, cyc_loss = 0.0134, total_loss = 0.1163
Epoch 131: loss = 0.1051, cyc_loss = 0.0136, total_loss = 0.1187
Epoch 132: loss = 0.1063, cyc_loss = 0.0131, total_loss = 0.1194
Epoch 133: loss = 0.1041, cyc_loss = 0.0133, total_loss = 0.1174
Epoch 134: loss = 0.1044, cyc_loss = 0.0133, total_loss = 0.1177
Epoch 135: loss = 0.1040, cyc_loss = 0.0129, total_loss = 0.1169
Epoch 136: loss = 0.1047, cyc_loss = 0.0127, total_loss = 0.1174
Epoch 137: loss = 0.1038, cyc_loss = 0.0134, total_loss = 0.1172
Epoch 138: loss = 0.1049, cyc_loss = 0.0129, total_loss = 0.1178
Epoch 139: loss = 0.1033, cyc_loss = 0.0133, total_loss = 0.1167
Epoch 140: loss = 0.1058, cyc_loss = 0.0130, total_loss = 0.1188
Epoch 141: loss = 0.1061, cyc_loss = 0.0131, total_loss = 0.1192
Epoch 142: loss = 0.1047, cyc_loss = 0.0130, total_loss = 0.1177
Epoch 143: loss = 0.1046, cyc_loss = 0.0126, total_loss = 0.1172
Epoch 144: loss = 0.1043, cyc_loss = 0.0128, total_loss = 0.1171
Epoch 145: loss = 0.1046, cyc_loss = 0.0129, total_loss = 0.1175
Epoch 146: loss = 0.1049, cyc_loss = 0.0127, total_loss = 0.1176
Epoch 147: loss = 0.1037, cyc_loss = 0.0130, total_loss = 0.1166
Epoch 148: loss = 0.1037, cyc_loss = 0.0131, total_loss = 0.1167
Epoch 149: loss = 0.1025, cyc_loss = 0.0129, total_loss = 0.1154
Epoch 150: loss = 0.1059, cyc_loss = 0.0127, total_loss = 0.1186
Epoch 151: loss = 0.1045, cyc_loss = 0.0123, total_loss = 0.1168
Epoch 152: loss = 0.1040, cyc_loss = 0.0131, total_loss = 0.1172
Epoch 153: loss = 0.1057, cyc_loss = 0.0124, total_loss = 0.1181
Epoch 154: loss = 0.1051, cyc_loss = 0.0126, total_loss = 0.1177
Epoch 155: loss = 0.1029, cyc_loss = 0.0121, total_loss = 0.1150
Epoch 156: loss = 0.1033, cyc_loss = 0.0125, total_loss = 0.1159
Epoch 157: loss = 0.1041, cyc_loss = 0.0126, total_loss = 0.1167
Epoch 158: loss = 0.1032, cyc_loss = 0.0123, total_loss = 0.1155
Epoch 159: loss = 0.1039, cyc_loss = 0.0124, total_loss = 0.1162
Epoch 160: loss = 0.1030, cyc_loss = 0.0126, total_loss = 0.1155
Epoch 161: loss = 0.1042, cyc_loss = 0.0123, total_loss = 0.1166
Epoch 162: loss = 0.1048, cyc_loss = 0.0123, total_loss = 0.1171
Epoch 163: loss = 0.1041, cyc_loss = 0.0124, total_loss = 0.1165
Epoch 164: loss = 0.1035, cyc_loss = 0.0122, total_loss = 0.1157
Epoch 165: loss = 0.1063, cyc_loss = 0.0122, total_loss = 0.1185
Epoch 166: loss = 0.1049, cyc_loss = 0.0121, total_loss = 0.1170
Epoch 167: loss = 0.1032, cyc_loss = 0.0121, total_loss = 0.1153
Epoch 168: loss = 0.1055, cyc_loss = 0.0122, total_loss = 0.1177
Epoch 169: loss = 0.1048, cyc_loss = 0.0118, total_loss = 0.1165
Epoch 170: loss = 0.1032, cyc_loss = 0.0121, total_loss = 0.1153
Epoch 171: loss = 0.1038, cyc_loss = 0.0120, total_loss = 0.1157
Epoch 172: loss = 0.1024, cyc_loss = 0.0120, total_loss = 0.1144
Epoch 173: loss = 0.1049, cyc_loss = 0.0125, total_loss = 0.1174
Epoch 174: loss = 0.1039, cyc_loss = 0.0119, total_loss = 0.1158
Epoch 175: loss = 0.1037, cyc_loss = 0.0118, total_loss = 0.1155
Epoch 176: loss = 0.1034, cyc_loss = 0.0118, total_loss = 0.1152
Epoch 177: loss = 0.1026, cyc_loss = 0.0121, total_loss = 0.1147
Epoch 178: loss = 0.1039, cyc_loss = 0.0120, total_loss = 0.1158
Epoch 179: loss = 0.1048, cyc_loss = 0.0120, total_loss = 0.1169
Epoch 180: loss = 0.1036, cyc_loss = 0.0119, total_loss = 0.1155
Epoch 181: loss = 0.1038, cyc_loss = 0.0116, total_loss = 0.1154
Epoch 182: loss = 0.1051, cyc_loss = 0.0119, total_loss = 0.1170
Epoch 183: loss = 0.1048, cyc_loss = 0.0119, total_loss = 0.1167
Epoch 184: loss = 0.1024, cyc_loss = 0.0119, total_loss = 0.1144
Epoch 185: loss = 0.1031, cyc_loss = 0.0121, total_loss = 0.1153
Epoch 186: loss = 0.1051, cyc_loss = 0.0118, total_loss = 0.1168
Epoch 187: loss = 0.1038, cyc_loss = 0.0118, total_loss = 0.1156
Epoch 188: loss = 0.1026, cyc_loss = 0.0116, total_loss = 0.1142
Epoch 189: loss = 0.1022, cyc_loss = 0.0114, total_loss = 0.1136
Epoch 190: loss = 0.1037, cyc_loss = 0.0114, total_loss = 0.1152
Epoch 191: loss = 0.1027, cyc_loss = 0.0117, total_loss = 0.1144
Epoch 192: loss = 0.1054, cyc_loss = 0.0115, total_loss = 0.1169
Epoch 193: loss = 0.1044, cyc_loss = 0.0117, total_loss = 0.1161
Epoch 194: loss = 0.1041, cyc_loss = 0.0114, total_loss = 0.1155
Epoch 195: loss = 0.1040, cyc_loss = 0.0115, total_loss = 0.1155
Epoch 196: loss = 0.1026, cyc_loss = 0.0118, total_loss = 0.1144
Epoch 197: loss = 0.1026, cyc_loss = 0.0116, total_loss = 0.1143
Epoch 198: loss = 0.1044, cyc_loss = 0.0113, total_loss = 0.1157
Epoch 199: loss = 0.1020, cyc_loss = 0.0113, total_loss = 0.1133
Epoch 200: loss = 0.1021, cyc_loss = 0.0117, total_loss = 0.1138
Epoch 201: loss = 0.1035, cyc_loss = 0.0113, total_loss = 0.1148
Epoch 202: loss = 0.1044, cyc_loss = 0.0113, total_loss = 0.1157
Epoch 203: loss = 0.1045, cyc_loss = 0.0116, total_loss = 0.1161
Epoch 204: loss = 0.1033, cyc_loss = 0.0115, total_loss = 0.1148
Epoch 205: loss = 0.1042, cyc_loss = 0.0113, total_loss = 0.1155
Epoch 206: loss = 0.1047, cyc_loss = 0.0115, total_loss = 0.1161
Epoch 207: loss = 0.1016, cyc_loss = 0.0115, total_loss = 0.1131
Epoch 208: loss = 0.1033, cyc_loss = 0.0114, total_loss = 0.1147
Epoch 209: loss = 0.1032, cyc_loss = 0.0115, total_loss = 0.1147
Epoch 210: loss = 0.1046, cyc_loss = 0.0115, total_loss = 0.1162
Epoch 211: loss = 0.1067, cyc_loss = 0.0113, total_loss = 0.1180
Epoch 212: loss = 0.1035, cyc_loss = 0.0111, total_loss = 0.1146
Epoch 213: loss = 0.1060, cyc_loss = 0.0114, total_loss = 0.1174
Epoch 214: loss = 0.1016, cyc_loss = 0.0116, total_loss = 0.1132
Epoch 215: loss = 0.1033, cyc_loss = 0.0114, total_loss = 0.1147
Epoch 216: loss = 0.1036, cyc_loss = 0.0111, total_loss = 0.1147
Epoch 217: loss = 0.1036, cyc_loss = 0.0116, total_loss = 0.1152
Epoch 218: loss = 0.1017, cyc_loss = 0.0111, total_loss = 0.1128
Epoch 219: loss = 0.1043, cyc_loss = 0.0111, total_loss = 0.1154
Epoch 220: loss = 0.1041, cyc_loss = 0.0113, total_loss = 0.1154
Epoch 221: loss = 0.1024, cyc_loss = 0.0117, total_loss = 0.1141
Epoch 222: loss = 0.1020, cyc_loss = 0.0115, total_loss = 0.1135
Epoch 223: loss = 0.1014, cyc_loss = 0.0112, total_loss = 0.1126
Epoch 224: loss = 0.1026, cyc_loss = 0.0115, total_loss = 0.1141
Epoch 225: loss = 0.1058, cyc_loss = 0.0112, total_loss = 0.1170
Epoch 226: loss = 0.1016, cyc_loss = 0.0110, total_loss = 0.1126
Epoch 227: loss = 0.1033, cyc_loss = 0.0111, total_loss = 0.1144
Epoch 228: loss = 0.1037, cyc_loss = 0.0111, total_loss = 0.1148
Epoch 229: loss = 0.1027, cyc_loss = 0.0113, total_loss = 0.1140
Epoch 230: loss = 0.1031, cyc_loss = 0.0109, total_loss = 0.1140
Epoch 231: loss = 0.1039, cyc_loss = 0.0112, total_loss = 0.1151
Epoch 232: loss = 0.1017, cyc_loss = 0.0111, total_loss = 0.1129
Epoch 233: loss = 0.1034, cyc_loss = 0.0111, total_loss = 0.1145
Epoch 234: loss = 0.1041, cyc_loss = 0.0112, total_loss = 0.1154
Epoch 235: loss = 0.1029, cyc_loss = 0.0109, total_loss = 0.1138
Epoch 236: loss = 0.1010, cyc_loss = 0.0113, total_loss = 0.1123
Epoch 237: loss = 0.1027, cyc_loss = 0.0110, total_loss = 0.1137
Epoch 238: loss = 0.1032, cyc_loss = 0.0108, total_loss = 0.1140
Epoch 239: loss = 0.1043, cyc_loss = 0.0109, total_loss = 0.1151
Epoch 240: loss = 0.1036, cyc_loss = 0.0111, total_loss = 0.1148
Epoch 241: loss = 0.1038, cyc_loss = 0.0110, total_loss = 0.1148
Epoch 242: loss = 0.1027, cyc_loss = 0.0114, total_loss = 0.1141
Epoch 243: loss = 0.1025, cyc_loss = 0.0109, total_loss = 0.1134
Epoch 244: loss = 0.1050, cyc_loss = 0.0107, total_loss = 0.1157
Epoch 245: loss = 0.1041, cyc_loss = 0.0111, total_loss = 0.1152
Epoch 246: loss = 0.1040, cyc_loss = 0.0108, total_loss = 0.1148
Epoch 247: loss = 0.1018, cyc_loss = 0.0112, total_loss = 0.1130
Epoch 248: loss = 0.1029, cyc_loss = 0.0108, total_loss = 0.1137
Epoch 249: loss = 0.1029, cyc_loss = 0.0109, total_loss = 0.1138
Epoch 250: loss = 0.1011, cyc_loss = 0.0111, total_loss = 0.1122
Epoch 251: loss = 0.1026, cyc_loss = 0.0110, total_loss = 0.1135
Epoch 252: loss = 0.1027, cyc_loss = 0.0110, total_loss = 0.1137
Epoch 253: loss = 0.1033, cyc_loss = 0.0112, total_loss = 0.1146
Epoch 254: loss = 0.1039, cyc_loss = 0.0106, total_loss = 0.1145
Epoch 255: loss = 0.1019, cyc_loss = 0.0108, total_loss = 0.1127
Epoch 256: loss = 0.1034, cyc_loss = 0.0109, total_loss = 0.1143
Epoch 257: loss = 0.1014, cyc_loss = 0.0108, total_loss = 0.1122
Epoch 258: loss = 0.1021, cyc_loss = 0.0107, total_loss = 0.1128
Epoch 259: loss = 0.1029, cyc_loss = 0.0108, total_loss = 0.1137
Epoch 260: loss = 0.1028, cyc_loss = 0.0107, total_loss = 0.1136
Epoch 261: loss = 0.1029, cyc_loss = 0.0110, total_loss = 0.1139
Epoch 262: loss = 0.1032, cyc_loss = 0.0107, total_loss = 0.1139
Epoch 263: loss = 0.1036, cyc_loss = 0.0107, total_loss = 0.1143
Epoch 264: loss = 0.1032, cyc_loss = 0.0109, total_loss = 0.1141
Epoch 265: loss = 0.1020, cyc_loss = 0.0110, total_loss = 0.1131
Epoch 266: loss = 0.1020, cyc_loss = 0.0108, total_loss = 0.1128
Epoch 267: loss = 0.1027, cyc_loss = 0.0107, total_loss = 0.1134
Epoch 268: loss = 0.1014, cyc_loss = 0.0107, total_loss = 0.1121
Epoch 269: loss = 0.1020, cyc_loss = 0.0108, total_loss = 0.1128
Epoch 270: loss = 0.1015, cyc_loss = 0.0107, total_loss = 0.1123
Epoch 271: loss = 0.1027, cyc_loss = 0.0107, total_loss = 0.1134
Epoch 272: loss = 0.1041, cyc_loss = 0.0108, total_loss = 0.1148
Epoch 273: loss = 0.1044, cyc_loss = 0.0106, total_loss = 0.1149
Epoch 274: loss = 0.1020, cyc_loss = 0.0107, total_loss = 0.1127
Epoch 275: loss = 0.1026, cyc_loss = 0.0107, total_loss = 0.1132
Epoch 276: loss = 0.1022, cyc_loss = 0.0109, total_loss = 0.1131
Epoch 277: loss = 0.1013, cyc_loss = 0.0108, total_loss = 0.1121
Epoch 278: loss = 0.1012, cyc_loss = 0.0107, total_loss = 0.1119
Epoch 279: loss = 0.1018, cyc_loss = 0.0106, total_loss = 0.1124
Epoch 280: loss = 0.1041, cyc_loss = 0.0107, total_loss = 0.1148
Epoch 281: loss = 0.1022, cyc_loss = 0.0107, total_loss = 0.1129
Epoch 282: loss = 0.1044, cyc_loss = 0.0107, total_loss = 0.1151
Epoch 283: loss = 0.1025, cyc_loss = 0.0106, total_loss = 0.1132
Epoch 284: loss = 0.1013, cyc_loss = 0.0105, total_loss = 0.1118
Epoch 285: loss = 0.1024, cyc_loss = 0.0107, total_loss = 0.1131
Epoch 286: loss = 0.1032, cyc_loss = 0.0106, total_loss = 0.1138
Epoch 287: loss = 0.1023, cyc_loss = 0.0106, total_loss = 0.1129
Epoch 288: loss = 0.1030, cyc_loss = 0.0105, total_loss = 0.1135
Epoch 289: loss = 0.1034, cyc_loss = 0.0106, total_loss = 0.1140
Epoch 290: loss = 0.1019, cyc_loss = 0.0106, total_loss = 0.1124
Epoch 291: loss = 0.1042, cyc_loss = 0.0108, total_loss = 0.1150
Epoch 292: loss = 0.1032, cyc_loss = 0.0105, total_loss = 0.1137
Epoch 293: loss = 0.1007, cyc_loss = 0.0108, total_loss = 0.1115
Epoch 294: loss = 0.1022, cyc_loss = 0.0105, total_loss = 0.1128
Epoch 295: loss = 0.1033, cyc_loss = 0.0106, total_loss = 0.1139
Epoch 296: loss = 0.1018, cyc_loss = 0.0107, total_loss = 0.1125
Epoch 297: loss = 0.1029, cyc_loss = 0.0107, total_loss = 0.1136
Epoch 298: loss = 0.1015, cyc_loss = 0.0109, total_loss = 0.1123
Epoch 299: loss = 0.1027, cyc_loss = 0.0105, total_loss = 0.1132
Epoch 300: loss = 0.1034, cyc_loss = 0.0106, total_loss = 0.1141

"""

# 각 줄을 분할하여 필요한 값을 추출하고 리스트에 저장
loss_list = [float(line.split(",")[0].split("=")[1]) for line in data.split("\n") if line.strip()]
cyc_loss_list = [float(line.split(",")[1].split("=")[1]) for line in data.split("\n") if line.strip()]
total_loss_list = [float(line.split(",")[2].split("=")[1]) for line in data.split("\n") if line.strip()]

# Epoch 번호 (1부터 시작)
epochs = range(1, len(loss_list) + 1)


# y축 범위 설정
plt.ylim(0.0, 0.3)
# y축 틱 설정
plt.yticks(np.arange(0.0, 0.3, 0.1))


# Loss 그래프
plt.plot(epochs, loss_list, label='Loss', color='blue')
# Cycle Loss 그래프
plt.plot(epochs, cyc_loss_list, label='Cycle Loss', color='red')
# Total Loss 그래프
plt.plot(epochs, total_loss_list, label='Total Loss', color='green')

plt.title('Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()
# 이미지로 저장
plt.savefig('Cycle6_tgt2_0506.png')
