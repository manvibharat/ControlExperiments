import matplotlib.pyplot as plt
from math import sin
from math import pi
import peakutils

import numpy as np
import scipy.io as sio

#----------------------------------------------------#
# Paste the contents of terminal Here

t = [0.002, 0.024, 0.036, 0.048, 0.05899999999999999, 0.071, 0.084, 0.095, 0.106, 0.118, 0.13, 0.141, 0.155, 0.166, 0.178, 0.19, 0.202, 0.214, 0.226, 0.237, 0.249, 0.26, 0.272, 0.284, 0.296, 0.307, 0.319, 0.33, 0.343, 0.355, 0.37, 0.383, 0.395, 0.406, 0.418, 0.43, 0.446, 0.458, 0.469, 0.48, 0.494, 0.506, 0.517, 0.529, 0.54, 0.5540000000000001, 0.5649999999999999, 0.577, 0.588, 0.6, 0.612, 0.624, 0.636, 0.6470000000000001, 0.659, 0.67, 0.683, 0.694, 0.706, 0.717, 0.729, 0.74, 0.754, 0.765, 0.777, 0.7890000000000001, 0.8, 0.8129999999999999, 0.825, 0.8359999999999999, 0.848, 0.86, 0.874, 0.885, 0.8970000000000001, 0.908, 0.9200000000000001, 0.932, 0.944, 0.9559999999999999, 0.967, 0.9789999999999999, 0.991, 1.003, 1.015, 1.026, 1.038, 1.05, 1.061, 1.074, 1.086, 1.097, 1.109, 1.12, 1.133, 1.145, 1.156, 1.168, 1.18, 1.191, 1.204, 1.216, 1.228, 1.239, 1.251, 1.264, 1.275, 1.287, 1.298, 1.31, 1.321, 1.334, 1.345, 1.358, 1.369, 1.381, 1.394, 1.406, 1.417, 1.429, 1.44, 1.455, 1.47, 1.481, 1.494, 1.505, 1.517, 1.528, 1.54, 1.552, 1.564, 1.576, 1.587, 1.599, 1.611, 1.624, 1.636, 1.648, 1.66, 1.671, 1.684, 1.695, 1.707, 1.718, 1.73, 1.741, 1.754, 1.766, 1.778, 1.789, 1.801, 1.814, 1.826, 1.837, 1.849, 1.86, 1.874, 1.886, 1.897, 1.909, 1.92, 1.932, 1.946, 1.958, 1.969, 1.981, 1.995, 2.007, 2.019, 2.03, 2.044, 2.055, 2.067, 2.08, 2.091, 2.106, 2.117, 2.13, 2.141, 2.154, 2.166, 2.177, 2.189, 2.2, 2.213, 2.225, 2.236, 2.248, 2.259, 2.271, 2.284, 2.295, 2.307, 2.318, 2.331, 2.346, 2.358, 2.37, 2.381, 2.394, 2.405, 2.417, 2.429, 2.44, 2.453, 2.465, 2.476, 2.488, 2.5, 2.512, 2.524, 2.535, 2.547, 2.558, 2.57, 2.582, 2.595, 2.607, 2.618, 2.63, 2.642, 2.654, 2.666, 2.678, 2.69, 2.703, 2.715, 2.727, 2.74, 2.751, 2.763, 2.775, 2.786, 2.798, 2.81, 2.822, 2.835, 2.846, 2.858, 2.87, 2.881, 2.898, 2.91, 2.922, 2.934, 2.946, 2.958, 2.97, 2.981, 2.995, 3.007, 3.018, 3.03, 3.042, 3.054, 3.066, 3.077, 3.089, 3.101, 3.114, 3.126, 3.137, 3.149, 3.16, 3.173, 3.184, 3.197, 3.209, 3.22, 3.232, 3.244, 3.256, 3.267, 3.279, 3.291, 3.304, 3.315, 3.326, 3.338, 3.35, 3.362, 3.374, 3.386, 3.397, 3.409, 3.42, 3.432, 3.444, 3.456, 3.467, 3.479, 3.491, 3.504, 3.515, 3.526, 3.538, 3.55, 3.561, 3.574, 3.585, 3.597, 3.608, 3.62, 3.632, 3.645, 3.656, 3.668, 3.679, 3.691, 3.704, 3.716, 3.727, 3.739, 3.75, 3.763, 3.775, 3.786, 3.798, 3.81, 3.821, 3.834, 3.846, 3.857, 3.869, 3.88, 3.893, 3.905, 3.916, 3.928, 3.94, 3.952, 3.964, 3.976, 3.987, 3.999, 4.01, 4.023, 4.035, 4.046, 4.059, 4.071, 4.084, 4.095, 4.106, 4.118, 4.13, 4.141, 4.155, 4.166, 4.178, 4.189, 4.201, 4.214, 4.226, 4.237, 4.249, 4.26, 4.274, 4.285, 4.296, 4.308, 4.32, 4.331, 4.344, 4.355, 4.366, 4.378, 4.39, 4.404, 4.416, 4.427, 4.439, 4.45, 4.462, 4.474, 4.486, 4.497, 4.509, 4.52, 4.533, 4.545, 4.556, 4.568, 4.58, 4.592, 4.604, 4.615, 4.627, 4.639, 4.65, 4.662, 4.674, 4.686, 4.697, 4.709, 4.721, 4.734, 4.745, 4.757, 4.769, 4.781, 4.794, 4.805, 4.816, 4.828, 4.84, 4.851, 4.865, 4.876, 4.888, 4.899, 4.911, 4.924, 4.936, 4.947, 4.959, 4.97, 4.984, 4.995, 5.007, 5.018, 5.03, 5.042, 5.054, 5.065, 5.077, 5.088, 5.1, 5.112, 5.125, 5.136, 5.148, 5.16, 5.171, 5.185, 5.196, 5.207, 5.22, 5.231, 5.247, 5.259, 5.271, 5.284, 5.295, 5.307, 5.318, 5.33, 5.342, 5.354, 5.366, 5.379, 5.392, 5.404, 5.416, 5.427, 5.439, 5.45, 5.462, 5.474, 5.486, 5.497, 5.509, 5.52, 5.534, 5.545, 5.556, 5.568, 5.58, 5.592, 5.604, 5.615, 5.627, 5.638, 5.65, 5.662, 5.674, 5.686, 5.697, 5.709, 5.72, 5.733, 5.745, 5.756, 5.768, 5.78, 5.791, 5.804, 5.815, 5.827, 5.839, 5.85, 5.862, 5.874, 5.886, 5.898, 5.91, 5.921, 5.934, 5.947, 5.958, 5.97, 5.982, 5.994, 6.006, 6.017, 6.029, 6.04, 6.054, 6.065, 6.077, 6.089, 6.101, 6.114, 6.126, 6.137, 6.149, 6.16, 6.173, 6.185, 6.196, 6.208, 6.22, 6.231, 6.244, 6.255, 6.267, 6.279, 6.29, 6.304, 6.315, 6.327, 6.338, 6.35, 6.362, 6.374, 6.386, 6.397, 6.409, 6.42, 6.433, 6.445, 6.457, 6.468, 6.48, 6.492, 6.505, 6.516, 6.528, 6.539, 6.551, 6.563, 6.575, 6.587, 6.598, 6.61, 6.622, 6.634, 6.645, 6.657, 6.669, 6.68, 6.693, 6.705, 6.716, 6.728, 6.74, 6.751, 6.764, 6.775, 6.787, 6.798, 6.81, 6.822, 6.834, 6.846, 6.857, 6.869, 6.88, 6.893, 6.905, 6.916, 6.928, 6.94, 6.953, 6.965, 6.976, 6.988, 7.0, 7.011, 7.024, 7.036, 7.047, 7.059, 7.07, 7.083, 7.095, 7.107, 7.118, 7.13, 7.141, 7.154, 7.165, 7.177, 7.188, 7.2, 7.214, 7.225, 7.236, 7.248, 7.26, 7.271, 7.284, 7.295, 7.308, 7.319, 7.331, 7.344, 7.356, 7.368, 7.379, 7.391, 7.404, 7.416, 7.427, 7.439, 7.45, 7.464, 7.475, 7.487, 7.498, 7.511, 7.524, 7.535, 7.546, 7.558, 7.57, 7.581, 7.594, 7.605, 7.617, 7.628, 7.64, 7.657, 7.669, 7.68, 7.693, 7.705, 7.717, 7.729, 7.74, 7.752, 7.764, 7.776, 7.787, 7.799, 7.81, 7.824, 7.835, 7.846, 7.858, 7.87, 7.881, 7.897, 7.909, 7.92, 7.934, 7.945, 7.956, 7.968, 7.98, 7.992, 8.004, 8.015000000000001, 8.026999999999999, 8.038, 8.050000000000001, 8.061999999999999, 8.074, 8.086, 8.097, 8.109, 8.122, 8.134, 8.145, 8.157, 8.167999999999999, 8.18, 8.192, 8.204000000000001, 8.215999999999999, 8.227, 8.239000000000001, 8.25, 8.262, 8.275, 8.286, 8.298, 8.31, 8.321, 8.334, 8.346, 8.356999999999999, 8.369, 8.380000000000001, 8.394, 8.404999999999999, 8.416, 8.428000000000001, 8.44, 8.451000000000001, 8.468, 8.48, 8.493, 8.506, 8.516999999999999, 8.529, 8.539999999999999, 8.553000000000001, 8.564, 8.576000000000001, 8.587, 8.599, 8.609999999999999, 8.624000000000001, 8.635, 8.647, 8.657999999999999, 8.67, 8.682, 8.694000000000001, 8.706, 8.717000000000001, 8.728999999999999, 8.74, 8.753, 8.765000000000001, 8.776, 8.788, 8.800000000000001, 8.811, 8.824, 8.836, 8.847, 8.859, 8.869999999999999, 8.885, 8.896000000000001, 8.907999999999999, 8.919, 8.930999999999999, 8.944000000000001, 8.956, 8.967000000000001, 8.978999999999999, 8.991, 9.004, 9.015000000000001, 9.026999999999999, 9.039, 9.050000000000001, 9.061999999999999, 9.074, 9.087, 9.098000000000001, 9.109999999999999, 9.122, 9.134, 9.146000000000001, 9.157, 9.169, 9.18, 9.193, 9.205, 9.215999999999999, 9.228, 9.24, 9.250999999999999, 9.265000000000001, 9.276, 9.289, 9.300000000000001, 9.311999999999999, 9.324, 9.336, 9.347, 9.359, 9.369999999999999, 9.384, 9.397, 9.409000000000001, 9.42, 9.433, 9.445, 9.456, 9.468, 9.48, 9.494, 9.505000000000001, 9.516999999999999, 9.528, 9.539999999999999, 9.552, 9.564, 9.574999999999999, 9.587, 9.599, 9.609999999999999, 9.622999999999999, 9.634, 9.646000000000001, 9.661, 9.673999999999999, 9.686, 9.698, 9.709, 9.720000000000001, 9.734, 9.746, 9.757, 9.769, 9.779999999999999, 9.794, 9.805, 9.816000000000001, 9.827999999999999, 9.84, 9.852, 9.865, 9.875999999999999, 9.888, 9.898999999999999, 9.911, 9.923999999999999, 9.935, 9.946999999999999, 9.959, 9.970000000000001, 9.984, 9.994999999999999, 10.007]
ang_pos = [0, 0, 0, 1, 2, 3, 4, 6, 9, 11, 15, 19, 24, 28, 33, 38, 42, 47, 52, 56, 61, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 105, 108, 111, 113, 117, 120, 123, 126, 128, 131, 133, 136, 138, 141, 143, 146, 148, 150, 152, 155, 156, 158, 160, 162, 164, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 177, 178, 178, 179, 179, 180, 180, 180, 180, 180, 180, 180, 179, 179, 179, 178, 178, 177, 176, 176, 174, 173, 172, 171, 170, 168, 167, 165, 163, 162, 160, 158, 156, 153, 151, 148, 146, 144, 141, 138, 136, 133, 130, 127, 124, 121, 118, 115, 111, 108, 105, 102, 98, 95, 90, 87, 83, 79, 76, 72, 68, 64, 60, 57, 53, 49, 45, 40, 36, 32, 28, 24, 20, 16, 12, 8, 5, 1, -4, -7, -12, -16, -20, -24, -28, -32, -36, -40, -44, -48, -52, -56, -60, -64, -67, -71, -75, -78, -83, -86, -90, -93, -97, -100, -104, -107, -110, -114, -117, -120, -123, -126, -129, -132, -134, -137, -140, -142, -144, -146, -149, -151, -153, -155, -157, -159, -161, -163, -165, -166, -168, -169, -170, -172, -172, -174, -174, -176, -176, -177, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -177, -176, -176, -174, -173, -172, -170, -168, -166, -164, -162, -160, -158, -156, -154, -150, -148, -145, -142, -140, -137, -134, -132, -128, -125, -122, -120, -117, -113, -110, -107, -104, -100, -96, -93, -90, -86, -82, -79, -75, -71, -67, -63, -59, -55, -52, -48, -44, -40, -36, -32, -28, -24, -20, -16, -11, -8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 47, 51, 55, 59, 63, 67, 70, 74, 78, 82, 84, 88, 92, 96, 99, 102, 105, 108, 112, 115, 118, 121, 124, 126, 130, 132, 135, 137, 140, 142, 145, 147, 149, 151, 153, 156, 158, 160, 161, 163, 164, 166, 168, 169, 170, 172, 172, 174, 175, 175, 176, 177, 178, 178, 179, 179, 180, 180, 180, 180, 180, 179, 179, 179, 179, 178, 178, 178, 177, 176, 176, 175, 174, 173, 172, 170, 169, 168, 166, 164, 163, 161, 159, 157, 154, 152, 150, 148, 145, 142, 140, 137, 135, 132, 129, 126, 123, 120, 117, 114, 111, 107, 104, 100, 97, 94, 90, 86, 82, 80, 76, 71, 67, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 17, 13, 8, 5, 1, -4, -7, -11, -16, -20, -24, -28, -32, -36, -40, -44, -48, -51, -55, -60, -64, -68, -72, -75, -79, -82, -85, -90, -92, -96, -100, -104, -107, -110, -113, -116, -120, -122, -125, -128, -131, -134, -136, -139, -141, -144, -146, -148, -151, -152, -155, -157, -158, -160, -162, -164, -166, -167, -168, -170, -171, -172, -173, -174, -175, -176, -176, -177, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -177, -177, -176, -176, -175, -174, -173, -171, -170, -168, -166, -164, -162, -160, -158, -155, -153, -151, -148, -146, -143, -140, -137, -134, -132, -129, -126, -124, -120, -117, -114, -111, -108, -104, -101, -98, -94, -90, -88, -84, -80, -76, -73, -69, -65, -61, -57, -53, -49, -46, -42, -37, -34, -29, -25, -21, -17, -13, -9, -6, -2, 3, 7, 11, 15, 19, 22, 27, 31, 34, 38, 42, 46, 50, 54, 58, 62, 65, 69, 73, 77, 81, 84, 87, 92, 94, 98, 101, 104, 108, 111, 114, 117, 120, 123, 126, 128, 131, 134, 136, 139, 142, 144, 146, 148, 151, 153, 155, 157, 159, 161, 163, 164, 166, 167, 168, 170, 171, 172, 174, 174, 176, 176, 177, 178, 178, 179, 179, 180, 180, 180, 180, 180, 180, 180, 180, 179, 179, 178, 178, 177, 177, 176, 175, 174, 173, 172, 170, 169, 167, 166, 164, 162, 160, 158, 156, 154, 151, 149, 146, 144, 141, 139, 136, 134, 131, 128, 125, 122, 118, 116, 112, 108, 106, 102, 99, 95, 92, 88, 85, 81, 78, 74, 70, 66, 62, 59, 55, 51, 47, 43, 39, 36, 31, 26, 23, 19, 15, 11, 7, 2, -2, -6, -9, -13, -19, -23, -27, -31, -35, -39, -43, -47, -51, -55, -58, -62, -66, -70, -73, -77, -81, -84, -87, -92, -94, -98, -101, -105, -108, -111, -114, -118, -120, -123, -126, -129, -132, -134, -137, -140, -142, -144, -147, -149, -152, -153, -155, -157, -159, -161, -163, -164, -166, -168, -169, -170, -172, -172, -174, -174, -176, -176, -177, -178, -178, -178, -178, -178, -178, -179, -179, -178, -178, -178, -178, -178, -178, -178, -178, -178, -178, -177, -176, -176, -174, -173, -172, -170, -168, -167, -164, -162, -160, -158, -156, -154, -151, -149, -146, -144, -141, -138, -136, -133, -130, -126, -123, -120, -117, -114, -111, -108, -104, -101, -97, -94, -90, -87, -83, -80, -76, -72, -68, -64, -60, -57, -53, -49, -45, -41, -37, -33, -29, -24, -20]
desd_pos = [0.6782383950791145, 8.136106978226351, 12.19896224733732, 16.25558262813768, 19.96690328642915, 24.00578180411304, 28.36732334739317, 32.04467278236265, 35.70826003001109, 39.68735628918324, 43.64616834476584, 47.25553200579571, 51.81971274314414, 55.38072384100281, 59.23828474706188, 63.06556897207043, 66.86062039146709, 70.6214993548739, 74.34628367745169, 77.72733490034684, 81.37763318873034, 84.68724760026687, 88.25620689964888, 91.78005846104629, 95.25700124429987, 98.40147255939202, 101.7835609435943, 104.8381508385968, 108.3899710135973, 111.6109161639121, 115.556688863577, 118.9018251649203, 121.9263858916565, 124.644193679877, 127.5479835273968, 130.3865836140655, 134.0674747569921, 136.7483823435218, 139.1445155133771, 141.4808904544561, 144.3664510457581, 146.7599296379962, 148.888087542968, 151.136757005765, 153.1302062433686, 155.5720997658824, 157.414890301706, 159.3480776940503, 161.0486442838721, 162.8249005700051, 164.5179370667285, 166.1268884632683, 167.6509324247366, 168.9727178534699, 170.3318827191442, 171.5013231957659, 172.7883924545276, 173.7965280258027, 174.8111713521456, 175.6627849570878, 176.5057652735149, 177.1992581196182, 177.9717855027406, 178.4919411003026, 178.9719500555652, 179.3604864661389, 179.636118317513, 179.8623941826493, 179.9755089636054, 179.9983914125303, 179.9351900874897, 179.780023905882, 179.4828717464527, 179.1617900855503, 178.7237700611964, 178.2420007514088, 177.6291380103524, 176.925489035701, 176.1314134623709, 175.2473171423034, 174.3581998961268, 173.3028659298445, 172.1589568871686, 170.9270574198895, 169.6077971516943, 168.322306289703, 166.8375270217258, 165.2674771113853, 163.7540413837352, 161.8748183446673, 160.0539434758256, 158.3129225744138, 156.3361108278105, 154.4538151195004, 152.1438284124996, 149.9305004188898, 147.834271266745, 145.4750973521067, 143.041571130643, 140.7465839285883, 137.9564742329771, 135.3075025492598, 132.5893752153424, 130.038193059708, 127.1914300938261, 124.0341241076092, 121.3043697883648, 118.267081324683, 115.4297614104377, 112.2780076556565, 109.3384488412747, 105.8039845033045, 102.7636282260036, 99.11368336837178, 95.97874453702373, 92.51184717380127, 88.70274050763662, 85.13936490201035, 81.8346659491417, 78.18950605056675, 74.81295757140578, 70.15707935048541, 65.44517547844518, 61.95634914799916, 57.79900360939772, 54.25407009664801, 50.36034874268808, 46.76844422335203, 42.82714894656593, 38.86396471849615, 34.88091712218125, 30.88004189282521, 27.19865814743625, 23.16933582727239, 19.12817166202491, 14.73927628275122, 10.68008116373667, 6.615427456372153, 2.547392604736415, -1.182833840822299, -5.590503177186386, -9.317556212570661, -13.37881316643665, -17.0956757201701, -21.14200619406876, -24.84170034569333, -29.20018755420117, -33.20791990479653, -37.19867969105101, -40.84022403928568, -44.7927601776379, -49.04877651801996, -52.95135163148609, -56.50498611067021, -60.35394923941416, -63.85511502563144, -68.27128527446193, -72.01888896154085, -75.42190320078034, -79.09729002349231, -82.43092642626168, -86.02719632937687, -90.1671454422655, -93.66585721883631, -96.83099812646454, -100.2364040725181, -104.1445068539203, -107.4367478789501, -110.6740779935353, -113.5919792340698, -117.2349535256991, -120.0402022678608, -123.0416359953905, -126.2221761428151, -128.8543418579913, -132.3542592580752, -134.8538451388358, -137.7331508989919, -140.1050256760051, -142.8304969237321, -145.2703111080599, -147.4416127100863, -149.738055870758, -151.7759262658333, -154.1002142818688, -156.1637000336068, -157.9851381705651, -159.8947530450043, -161.5734657466966, -163.325624693137, -165.1295698230648, -166.5786625938251, -168.0778789207468, -169.3767136793706, -170.8178754728468, -172.3533836162115, -173.4827466574534, -174.523442685281, -175.3990674459882, -176.3367516917302, -177.0475829357159, -177.736306306973, -178.3341886709301, -178.8021843899171, -179.2562546515029, -179.5799670002937, -179.7960774415514, -179.9437665156596, -179.9994863497892, -179.963208465539, -179.8349514045317, -179.6366364302358, -179.3323092971559, -178.9728202428326, -178.4929943718356, -177.9219407503488, -177.2006909795004, -176.4405708607439, -175.664564251083, -174.7319821670021, -173.7100945853703, -172.5994237928224, -171.4005374530825, -170.1140483168318, -168.7406139085311, -167.1554265240869, -165.6031618128511, -163.9662573431792, -162.0984019177809, -160.4419184471045, -158.5562853099376, -156.5896140721678, -154.7165001359149, -152.5973503940846, -150.4002081626548, -148.1261964007869, -145.577287462549, -143.352251968402, -140.8547592603781, -138.2852756998374, -135.8677947783929, -132.0172941544876, -129.2175273824133, -126.3517175458006, -123.4213293597531, -120.4278605453617, -117.3728410642201, -114.2578323364609, -111.3510679969672, -107.5825523247237, -104.2927286190718, -101.2301892850029, -97.8396999462591, -94.39920474725094, -90.91046212471005, -87.37525517462059, -84.09537394447913, -80.47618025649703, -76.81585520132237, -72.80625772120075, -69.06627418673804, -65.60689911407984, -61.80095232652072, -58.28437218504358, -54.09626073370275, -50.52702857698452, -46.28098889958678, -42.33686979515668, -38.70236918480122, -34.71855686084897, -30.71699988616792, -26.69974345610353, -23.00522032507886, -18.96361828091994, -14.9123239334692, -10.51488586674665, -6.788944688580803, -3.060087870453645, 1.009199420290492, 5.077970909317969, 9.144147047952341, 13.20564961400048, 17.26040277393169, 20.96956063389019, 25.00558866326771, 28.69410406242189, 32.70382984959597, 36.69684071280315, 40.6710958246145, 44.29595159603202, 48.22858963804027, 52.1365780530004, 56.34009948449381, 59.87063013119747, 63.37544820993401, 67.1677926389377, 70.92580761624851, 74.33885645251924, 78.33118485902573, 81.67270548680342, 85.27794762411494, 88.54450879301636, 92.06461226161267, 95.53766151664787, 99.24497400378412, 102.3355220422558, 105.656858927035, 108.6540201111436, 111.8703869977503, 115.2902110388798, 118.3856381296211, 121.1699974018047, 124.1480895502562, 126.8223030355988, 129.9124279487266, 132.6957280460017, 135.1875419026766, 137.8396321123192, 140.4212725006104, 142.7247604033759, 145.3679625899052, 147.7304840381289, 149.8298284040853, 152.046604075923, 154.0104084268835, 156.2459291342288, 158.226332246105, 159.9706841554846, 161.7952335823769, 163.5370894825476, 165.1953615936312, 166.7692023729273, 168.2578074305809, 169.5468342736137, 170.8699817829542, 172.0061642983459, 173.2536502875777, 174.3129529901408, 175.2057286095621, 176.1637885249896, 176.9543753954295, 177.7087723897091, 178.2638672045325, 178.7424032493628, 179.1768869969929, 179.519793456685, 179.7535257564301, 179.9393428275823, 179.9975310527756, 179.9728450173714, 179.8694095286174, 179.6684718676695, 179.3471678021398, 178.9550910151755, 178.5153330515155, 177.9481663674377, 177.3483592483674, 176.4748489173682, 175.7023623457502, 174.8544170905694, 173.843754364009, 172.7442401130336, 171.658777604142, 170.2809500090924, 169.0352835995622, 167.71702180881, 166.1967893930014, 164.5916138157635, 162.6126471582138, 160.8262998453966, 159.1165828527262, 157.1735267252986, 155.321798096135, 153.2256809863498, 151.0512502472658, 148.7996172302034, 146.6687824192944, 144.2724282499017, 142.0109632479142, 139.2597695064449, 136.6460269017329, 134.1887106468782, 131.4423125184093, 128.6287342379548, 125.7494138250761, 122.8058229001298, 120.0523557077379, 116.989812246742, 113.8674753051161, 110.9541686119113, 107.7217134735002, 104.4342017787592, 101.0933137745675, 97.98540137398721, 94.54700412313834, 91.06028390851129, 87.23054000168368, 83.94902662429963, 80.32812411755868, 76.66616591510179, 72.96502364337865, 68.9134291551132, 65.45277256597105, 61.96400605282206, 58.12778060993328, 54.26184606454127, 50.69366139302737, 46.1210504627576, 42.50561645582454, 38.54074093995038, 34.88891779059063, 30.88807624640579, 26.53608046830955, 22.50466643113624, 18.79904887180746, 14.74740417280584, 11.02672453423039, 6.284675351049736, 2.55554707771535, -1.513789216625627, -5.243385230601286, -9.309411844199534, -13.37068041839107, -17.42511523923971, -21.13390732987035, -25.16945584617459, -28.85745811069102, -32.86654411102413, -36.85883202414844, -41.16248808873517, -44.78486138543337, -48.71455184082819, -52.61934429394461, -56.17516043067313, -60.66565270252505, -64.16444598947566, -67.63568264849448, -71.70048796825713, -75.10644353756851, -80.00258757927266, -83.62723382834952, -87.2091382070875, -91.0391788575873, -94.23742129079631, -97.68020784102859, -100.7922808501562, -104.1378550849488, -107.4302044730535, -110.6676462950481, -113.8485258947601, -117.2287650407512, -120.5386870818291, -123.5298703951585, -126.4579176048324, -129.0852188451149, -131.88810039504, -134.3982267789992, -137.0706806278092, -139.6730776662899, -142.2040878095913, -144.4603635536543, -146.8509647402529, -148.9764441134926, -151.5889484893018, -153.5677402901847, -155.4805795371844, -157.4911300957786, -159.4211869544871, -161.2697636614536, -163.0359154093197, -164.5817080997349, -166.1873919259749, -167.584672033247, -169.0268734777191, -170.3826853050861, -171.6514145600674, -172.8324127952748, -173.8374089211164, -174.8486074209328, -175.6970464167741, -176.6024379574977, -177.3441736116453, -177.9444811494558, -178.5121955424874, -178.988672371313, -179.3450843110661, -179.6669859832956, -179.8551953733217, -179.9724183950368, -179.9976575328008, -179.9399762682143, -179.7889170634397, -179.5459677622253, -179.211252535933, -178.7849424574794, -178.2672554139005, -177.7126619807714, -176.9588553580643, -176.0989038451228, -175.2887269191591, -174.3190527196469, -173.2602840707805, -172.1129621091044, -170.877673230751, -169.6685870263162, -168.2664977481075, -166.9056814927983, -165.0701431331607, -163.5473097960648, -161.8059537924236, -159.9818987829625, -158.076077042004, -155.9202960765766, -153.8473033667282, -151.8779580297033, -149.6552203312934, -147.5504890975258, -144.9814537671666, -142.5328136630448, -140.2242003079244, -137.6370651195907, -134.9795836418747, -132.4829210937556, -129.4590500320851, -126.8396637343501, -123.9200639097719, -120.9371285536747, -118.148434170255, -114.5259607532099, -111.6237122382076, -108.4029924586612, -105.4019537777318, -102.0765118071495, -98.69889854220981, -95.27084028069529, -91.79408910281863, -88.56580903985821, -85.00071713815395, -81.69450714416953, -77.74204608445018, -74.05217683845624, -70.32445953273585, -66.87576374129904, -63.08084542715974, -59.25368649961394, -55.07348407875867, -51.51048652482281, -47.59840302626325, -43.99090640273979, -40.03396223407945, -36.05655671156851, -32.06072268674636, -28.04850242996051, -24.35799027232831, -20.32010118590569, -16.27182649792305, -12.21523528114272, -8.491158195742161, -4.424424936265781, -0.3554303536741194, 3.374691684356529, 7.781024037211225, 11.84432530452912, 15.5637508100842, 19.61362753398778, 23.65347973493991, 27.34610775809924, 31.69485767469705, 35.35982411835572, 39.34059559929214, 42.97202217392049, 46.91247673125463, 50.8289543267083, 54.71945324899667, 58.58198506453448, 62.09638458010769, 65.8998078319645, 69.35673811850084, 73.40368346663202, 77.10030061940185, 80.45429505454385, 84.07374157699275, 87.65021801903979, 91.47412409645437, 94.95523513817599, 98.10366289933333, 101.4902132156956, 104.824891894849, 107.8346567698434, 111.3318443085356, 114.5007923403802, 117.3542909891386, 120.4096758281923, 123.1564204274111, 126.3342912355917, 129.2004937336313, 132.0006618730284, 134.5082503909898, 137.1778818065445, 139.563485503996, 142.3054812208324, 144.5590250717914, 146.946597727263, 149.0692579707771, 151.3118413285929, 153.8303668544668, 155.7342209549132, 157.5711920656148, 159.4979545235803, 161.3431975939079, 162.9622516660047, 164.7853953040685, 166.2508946785692, 167.8907488677402, 169.1996978611677, 170.5447483580417, 171.9035021862235, 173.066233998109, 174.1405116761563, 175.0470919679388, 175.9503366947846, 176.8273569801941, 177.5427836495616, 178.1188851155818, 178.6601078206524, 179.0760184772891, 179.4941094326338, 179.7350239557257, 179.9098015641662, 179.9892385428084, 179.9834588073401, 179.8697199395612, 179.6892049595329, 179.4315190714094, 179.0625250169636, 178.6020121249756, 178.0996787409433, 177.4074179557063, 176.7385241547459, 175.9222647892806, 175.0950292183807, 174.1068407148522, 172.554709615022, 171.3524248212912, 170.1733796132215, 168.6857798642222, 167.2227826228387, 165.6743178349949, 164.0411769208797, 162.4704575847938, 160.6773904651995, 158.8022011483824, 156.8458480434033, 154.9820774773104, 152.8729902838005, 150.8709953450463, 148.2294069429593, 146.0814394039573, 143.8707344437663, 141.3886208787989, 138.8342436046979, 136.4303638188714, 132.8295014986704, 130.0494703076942, 127.4426825738791, 124.0459436627329, 121.3164197225351, 118.5347941645525, 115.4422762099126, 112.2907557201474, 109.0818434370448, 105.8171794353328, 102.7770190112464, 99.41018505564251, 96.27924425348537, 92.81656113180436, 89.30643947557522, 85.75067330760252, 82.1510799795986, 78.81452271129632, 75.13608803330479, 71.1078409006137, 67.35154628095716, 63.87798907537003, 60.05741790499214, 56.52821472935457, 52.65053962799789, 48.74595484142286, 44.81645600249852, 40.86405147766584, 37.22261707847624, 33.23196551041096, 29.5588975878556, 25.53749089987165, 21.1663025262035, 17.45758290874886, 13.40321124572657, 9.341989202858022, 5.614957199447491, 1.207299178548714, -2.86201116368415, -6.590978047429028, -10.65565829218541, -14.37688157922485, -19.10384414487212, -22.80872753883609, -26.50381529584485, -30.5217836392441, -34.52415230226263, -38.17753910628101, -43.79087333543803, -47.72652182030649, -51.96255140951657, -56.16741240134529, -59.69915746085917, -63.52267703458643, -66.99909651217948, -71.07037927470053, -74.4821111281477, -78.16746825853002, -81.51066171661723, -85.11780810433008, -88.38618676116663, -92.49085906621088, -95.67096270735858, -99.09325960154909, -102.1859157218834, -105.5096255785854, -108.7794094768462, -111.9935962304617, -115.1505430689235, -117.9927487413691, -121.0355014193425, -123.7703853895106, -126.9338995461781, -129.7865303243835, -132.3432043756508, -135.0674433620069, -137.7226493923876, -140.0947850440413, -142.8205702594802, -145.2606795493776, -147.4322559930132, -149.7290035597586, -151.7671570619441, -154.4412499399307, -156.323983368951, -158.3012785626181, -160.0427478579333, -161.8641173607458, -163.7438824172112, -165.3918989469922, -166.8283417302724, -168.3136359651645, -169.7129051185684, -171.130874726296, -172.250551848581, -173.387632434215, -174.4360946193039, -175.3188776729244, -176.1960290082458, -176.9831265718314, -177.7337269571864, -178.2855974739504, -178.8003051197439, -179.2236279485572, -179.5553496001371, -179.7953005315828, -179.9345319458923, -179.9982863164012, -179.9759108799077, -179.849818177149, -179.637671549438, -179.3625453363391, -178.9745595152112, -178.4950998157, -177.9754462911903, -177.2035556080208, -176.5105609510221, -175.5938594741213, -174.7358986051589, -173.7143679537875, -172.6040519073815, -171.4055179483547, -170.2298872138407, -168.8640193890924, -167.5361383023123, -165.7421239853129, -163.9729860088743, -162.2526125640561, -160.6027320373515, -158.5640054620247, -156.5976570515095, -154.724835433036, -152.6060004963401, -150.4091686489783, -147.7491188548622, -145.5868796920125, -143.1567966143753, -140.8649139351537, -138.2957163217956, -135.6558357824944, -132.9466215599145, -130.4034494668651, -127.5652457286877, -124.6618434069495, -121.9443829309485, -118.6654112918204, -115.8352215116359, -112.6910473837249, -108.6800259447052, -105.1334876777643, -101.8037387937131, -98.42195802956336, -95.27775950555055, -92.09264215603531, -87.98183638832784, -84.40946498719276, -81.09684749524769, -77.44341069324804, -74.05960994000708, -69.70714615109703, -66.25318164329325, -62.77076346075223, -58.94106822343285, -55.08124821239607, -51.19327618124068, -46.95184276027155, -43.34083799981257, -39.38038522986018, -35.73223932610324, -31.73499620701982, -27.38641019919698, -23.6939019897166, -19.65416069389829, -15.60437415863352, -11.88501308757588, -7.144108912834373, -3.415460891985336, 0.6537726855940681]
f = 0.3


#----------------------------------------------------------------------#
# Plots
plt.figure(1)
plt.plot(t, desd_pos) 
plt.xlabel('time') 
plt.ylabel('Angular Position') 
plt.plot(t,ang_pos)
plt.title('Input and output') 


#----------------------------------------------------------------#
# To find the magnitude ratio

t=np.asarray(t)
ang_pos=np.asarray(ang_pos)
desd_pos=np.asarray(desd_pos)

ang_pos_pks=peakutils.indexes(ang_pos, thres=0.5/max(ang_pos), min_dist=1)
ang_pos_mean=np.mean(ang_pos[ang_pos_pks])

desd_pos_pks=peakutils.indexes(desd_pos, thres=0.5/max(desd_pos), min_dist=1)
desd_pos_mean=np.mean(desd_pos[desd_pos_pks])

#-------------------------------------------------------------------#
# To save magnitude
mag=np.loadtxt('cl_mag.dat')
mag=np.append(mag,[ang_pos_mean/desd_pos_mean])
np.savetxt('cl_mag.dat', mag)

freq=np.loadtxt('cl_freq.dat')
freq=np.append(freq,[f])
np.savetxt('cl_freq.dat', freq)

plt.figure(2)
plt.semilogx(2*pi*freq, 20*np.log10(mag))
plt.xlabel('Angular frequency')
plt.ylabel('Magnitude in dB')
plt.title('Magnitude Bode Plot')


#-----------------------------------------------------#
# To save the data at the end
# np.savetxt('cl_data.dat', [freq,mag])

#-----------------------------------------------------#
# Saved data

data=np.loadtxt('cl_data.dat')
plt.figure(3)
plt.semilogx(data[0],20*np.log10(data[1]))
plt.xlabel('Angular frequency')
plt.ylabel('Magnitude in dB')
plt.title('Magnitude Bode Plot')

#-------------------------------------------------------#
# To get data from .mat File
# data=sio.loadmat('closedloopDat2.mat')
# print(data.keys())
# ol_mag=data.get('mag1')
# ol_mag=np.asarray(ol_mag)
# freq=data.get('freq')
# freq=np.asarray(freq)
# np.savetxt('cl_data.dat', [freq[0],ol_mag[0]])

#-------------------------------------------------------#

plt.show()