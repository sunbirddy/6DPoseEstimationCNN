import cv2
import numpy as np
import math


def eulerAnglesToRotationMatrix(theta):
        R_x = np.array([[1, 0, 0],
                        [0, math.cos(theta[0]), -math.sin(theta[0])],
                        [0, math.sin(theta[0]), math.cos(theta[0])]
                        ])

        R_y = np.array([[math.cos(theta[1]), 0, math.sin(theta[1])],
                        [0, 1, 0],
                        [-math.sin(theta[1]), 0, math.cos(theta[1])]
                        ])

        R_z = np.array([[math.cos(theta[2]), -math.sin(theta[2]), 0],
                        [math.sin(theta[2]), math.cos(theta[2]), 0],
                        [0, 0, 1]
                        ])

        R = np.dot(R_z, np.dot(R_y, R_x))

        return R

# pt3d =np.array([-0.0221253091278751, -0.03222454341149090, -0.0531708625729459,
#         -0.0485408095687060, 0.01801089070724520, -0.0914087341601877,
#         0.0251558108495496, -0.02874593475604420, -0.0474420406069757,
#         0.0501877722090462, 0.00169995567405297, -0.0850052203390318,
#         -0.0189187257994219, -0.06240228020575400, 0.0175843269951942,
#         -0.0283891350572715, 0.00911712129564941, 0.0631507331059011,
#         0.0213442276319188, -0.03674632360129580, 0.0159373489636849,
#         0.0318736703296913, 0.00542144271022592, 0.0599133788372898
#                 ]);

# pt3d =np.array([
# -0.023171, -0.025696, -0.053267,
# -0.050219, 0.019052, -0.091633,
# 0.023950, -0.028586 ,-0.046496,
# 0.050188, 0.001700, -0.085005])



# pt3d = np.array([-0.036600, -0.014582, -0.029238,
# -0.024315, -0.027407, -0.067659,
# 0.040232, -0.015307, -0.007439,
# 0.037394, -0.017777, -0.072696])


# pt3d =np.array([
#
# -0.048369, 0.019413, -0.091861,
# -0.028785, 0.010920, 0.063521,
# -0.016580, -0.074401, 0.020880,
# -0.023269, -0.026269, -0.054962,
# 0.020053, -0.028909, 0.015033,
# 0.032167, 0.002867, 0.060980,
# 0.025674, -0.028250, -0.046709,
# 0.050188, 0.001700, -0.085005,
# ])

pt3d =np.array([
-0.0244073998183012,	-0.0330047570168972,	-0.0480035655200481,
-0.0292589478194714,	0.0340714007616043,	-0.0565250627696514,
0.0250262394547462,	-0.0295181218534708,	-0.0519644841551781,
0.0268154423683882,	0.0409414395689964,	-0.0520650632679462,
-0.0191895309835672,	-0.0433797538280487,	0.0151688680052757,
-0.0274073854088783,	0.0197330769151449,	0.0425410605967045,
0.0220928564667702,	-0.0308573991060257,	0.0201466027647257,
0.0260033234953880,	0.0235524158924818,	0.0391192212700844])
pt3d = pt3d.reshape([8,3])



# pt2d = np.array([381.297474275023,   212.765201122544,
#         371.800000000000,   226,
#         407.645040548971,   207.379912663755,
#         424,                222,
#         377.653361344538,   177.581932773109,
#         374.164179104478,   144.259701492537,
#         402.236614853195,   173.443868739206,
#         407.943262411348,   143.342789598109
#                  ]);

pt2d = np.array([
371.800000000000,	226,
374.164179104478,	144.259701492537,
377.653361344538,	177.581932773109,
381.297474275023,	212.765201122544,
402.236614853195,	173.443868739206,
407.943262411348,	143.342789598109,
407.645040548971,	207.379912663755,
424,	            222])

pt2d = np.array([
381.0,	213.0,
372.0,	226.0,
408.0,	207.0,
424.0,	222.0,
378.0,	177.0,
374.0,	144.0,
402.0,	173.0,
408.0,	143.0])

pt2d = pt2d.reshape([8,2])

K = np.zeros((3, 3));

K[0, 0] = 572.41140
K[0, 2] = 325.2611
K[1, 1] = 573.57043
K[1, 2] = 242.04899
K[2, 2] = 1

# objectPoints = np.random.random((10,3,1))
#
# imagePoints = np.random.random((10,2,1))
#
# cameraMatrix = np.eye(3)

distCoeffs = np.zeros((5,1))

x=cv2.solvePnP(pt3d, pt2d, K, distCoeffs)
rot = eulerAnglesToRotationMatrix(x[1])
trans = x[2]
print rot
print trans
# r=[ 0.97441399  0.18984599 -0.12032   ;
#         -0.0544436  -0.320014   -0.94584697;
#         -0.218069    0.92819703 -0.30149001];
#     t=[  121.14949491;
#         -113.72310242;
#         1030.73827876]/1000;