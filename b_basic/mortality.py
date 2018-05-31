from utils import *

# the table gives the qx

mortality_tables = DataDict(
	test = DataDict(
		age_start = 1,
		age_end = 5,
		female = [0.5, 0.5, 0.5, 0.5, 0.5],
		male = [0.5, 0.5, 0.5, 0.5, 0.5],
	),

	gam83 = DataDict(
		age_start = 5,
		age_end = 110,
		female = [0.00019, 0.000156, 0.000131, 0.000116, 0.000108, 0.000107, 0.000116, 0.000126, 0.000135, 0.000146, 0.000156, 0.000166, 0.000177, 0.000187, 0.000199, 0.00021, 0.000223, 0.000236, 0.00025, 0.000265, 0.000281, 0.000298, 0.000315, 0.000335, 0.000356, 0.00038, 0.000404, 0.000431, 0.00046, 0.000492, 0.000529, 0.000558, 0.000595, 0.000637, 0.000686, 0.000739, 0.000796, 0.000861, 0.000935, 0.001021, 0.001122, 0.001241, 0.001374, 0.001518, 0.001672, 0.00183, 0.001992, 0.002165, 0.002355, 0.002572, 0.002823, 0.003114, 0.003448, 0.003825, 0.004246, 0.004712, 0.005225, 0.005789, 0.00641, 0.007095, 0.007849, 0.008686, 0.009646, 0.01078, 0.012135, 0.013761, 0.015698, 0.017955, 0.020534, 0.023435, 0.026658, 0.030205, 0.03408, 0.038288, 0.042832, 0.047717, 0.05295, 0.058546, 0.064523, 0.070897, 0.077687, 0.085078, 0.093189, 0.10215, 0.112616, 0.124167, 0.136751, 0.1507, 0.166197, 0.183448, 0.202688, 0.224174, 0.246715, 0.270999, 0.297983, 0.327986, 0.361361, 0.398774, 0.439825, 0.487067, 0.542018, 0.60654, 0.682566, 0.772094, 0.877193, 1.0],
		male = [0.00038, 0.000353, 0.000336, 0.000327, 0.000324, 0.000325, 0.000331, 0.000338, 0.000344, 0.000352, 0.000361, 0.00037, 0.000381, 0.000392, 0.000405, 0.000419, 0.000435, 0.000453, 0.000471, 0.000493, 0.000515, 0.000542, 0.00057, 0.000602, 0.000636, 0.000674, 0.000717, 0.000763, 0.000815, 0.000872, 0.000955, 0.001008, 0.001073, 0.001154, 0.001253, 0.001375, 0.001522, 0.001697, 0.001905, 0.002147, 0.002426, 0.002745, 0.0031, 0.003487, 0.003903, 0.004343, 0.004804, 0.005283, 0.005778, 0.006289, 0.006812, 0.007353, 0.007932, 0.008577, 0.009315, 0.010175, 0.011182, 0.01237, 0.013768, 0.015409, 0.017324, 0.019532, 0.022004, 0.024699, 0.027574, 0.030589, 0.033727, 0.037078, 0.040756, 0.044876, 0.049552, 0.054876, 0.060842, 0.06742, 0.074583, 0.0823, 0.090538, 0.099244, 0.108361, 0.11783, 0.127595, 0.137967, 0.148744, 0.160081, 0.172066, 0.184785, 0.198016, 0.211622, 0.225563, 0.242116, 0.260096, 0.27604, 0.293282, 0.312003, 0.332393, 0.35465, 0.378984, 0.405613, 0.43678, 0.474728, 0.521701, 0.579939, 0.651687, 0.739187, 0.844683, 1.0],
	),

	up94 = DataDict(
		age_start = 1,
		age_end = 120,
		female = [0.000571, 0.000372, 0.000278, 0.000208, 0.000188, 0.000176, 0.000165, 0.000147, 0.00014, 0.000141, 0.000148, 0.000159, 0.000177, 0.000203, 0.000233, 0.000261, 0.000281, 0.000293, 0.000301, 0.000305, 0.000308, 0.000311, 0.000313, 0.000313, 0.000313, 0.000316, 0.000324, 0.000338, 0.000356, 0.000377, 0.000401, 0.000427, 0.000454, 0.000482, 0.000514, 0.00055, 0.000593, 0.000643, 0.000701, 0.000763, 0.000826, 0.000888, 0.000943, 0.000992, 0.001046, 0.001111, 0.001196, 0.001297, 0.001408, 0.001536, 0.001686, 0.001864, 0.002051, 0.002241, 0.002466, 0.002755, 0.003139, 0.003612, 0.004154, 0.004773, 0.005476, 0.006271, 0.007179, 0.008194, 0.009286, 0.010423, 0.011574, 0.012648, 0.013665, 0.014763, 0.016079, 0.017748, 0.019724, 0.021915, 0.024393, 0.027231, 0.030501, 0.034115, 0.038024, 0.042361, 0.04726, 0.052853, 0.058986, 0.065569, 0.072836, 0.081018, 0.090348, 0.100882, 0.112467, 0.125016, 0.138442, 0.15266, 0.167668, 0.183524, 0.200229, 0.217783, 0.236188, 0.255605, 0.276035, 0.297233, 0.318956, 0.34096, 0.364586, 0.389996, 0.41518, 0.438126, 0.456824, 0.471493, 0.483473, 0.492436, 0.498054, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0],
		male = [0.000637, 0.00043, 0.000357, 0.000278, 0.000255, 0.000244, 0.000234, 0.000216, 0.000209, 0.000212, 0.000223, 0.000243, 0.000275, 0.00032, 0.000371, 0.000421, 0.000463, 0.000495, 0.000521, 0.000545, 0.00057, 0.000598, 0.000633, 0.000671, 0.000711, 0.000749, 0.000782, 0.000811, 0.000838, 0.000862, 0.000883, 0.000902, 0.000912, 0.000913, 0.000915, 0.000927, 0.000958, 0.00101, 0.001075, 0.001153, 0.001243, 0.001346, 0.001454, 0.001568, 0.001697, 0.001852, 0.002042, 0.00226, 0.002501, 0.002773, 0.003088, 0.003455, 0.003854, 0.004278, 0.004758, 0.005322, 0.006001, 0.006774, 0.007623, 0.008576, 0.009663, 0.010911, 0.012335, 0.013914, 0.015629, 0.017462, 0.019391, 0.021354, 0.023364, 0.025516, 0.027905, 0.030625, 0.033549, 0.036614, 0.040012, 0.043933, 0.04857, 0.053991, 0.060066, 0.066696, 0.07378, 0.081217, 0.088721, 0.096358, 0.104559, 0.113755, 0.124377, 0.136537, 0.149949, 0.164442, 0.179849, 0.196001, 0.213325, 0.231936, 0.251189, 0.270441, 0.289048, 0.30675, 0.323976, 0.341116, 0.35856, 0.376699, 0.396884, 0.418855, 0.440585, 0.460043, 0.4752, 0.48567, 0.492807, 0.497189, 0.499394, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0],
	),

	mgdb = DataDict(
		age_start = 1,
		age_end = 115,
		female = [0.000628, 0.000409, 0.000306, 0.000229, 0.000207, 0.000194, 0.000181, 0.000162, 0.000154, 0.000155, 0.000163, 0.000175, 0.000195, 0.000223, 0.000256, 0.000287, 0.000309, 0.000322, 0.000331, 0.000335, 0.000339, 0.000342, 0.000344, 0.000344, 0.000344, 0.000348, 0.000356, 0.000372, 0.000392, 0.000415, 0.000441, 0.00047, 0.000499, 0.00053, 0.000565, 0.000605, 0.000652, 0.000707, 0.000771, 0.000839, 0.000909, 0.000977, 0.001037, 0.001091, 0.001151, 0.001222, 0.001316, 0.001427, 0.001549, 0.00169, 0.001855, 0.00205, 0.002256, 0.002465, 0.002713, 0.00303, 0.003453, 0.003973, 0.004569, 0.00525, 0.006024, 0.006898, 0.007897, 0.009013, 0.010215, 0.011465, 0.012731, 0.013913, 0.015032, 0.016239, 0.017687, 0.019523, 0.021696, 0.024107, 0.026832, 0.029954, 0.033551, 0.037527, 0.041826, 0.046597, 0.051986, 0.058138, 0.064885, 0.072126, 0.08012, 0.08912, 0.099383, 0.11097, 0.123714, 0.137518, 0.152286, 0.167926, 0.184435, 0.201876, 0.220252, 0.239561, 0.259807, 0.281166, 0.303639, 0.326956, 0.350852, 0.375056, 0.401045, 0.428996, 0.456698, 0.481939, 0.502506, 0.518642, 0.53182, 0.54168, 0.547859, 0.55, 0.55, 0.55, 1.0],
		male = [0.000701, 0.000473, 0.000393, 0.000306, 0.00028, 0.000268, 0.000257, 0.000238, 0.00023, 0.000233, 0.000245, 0.000267, 0.000302, 0.000352, 0.000408, 0.000463, 0.000509, 0.000544, 0.000573, 0.000599, 0.000627, 0.000658, 0.000696, 0.000738, 0.000782, 0.000824, 0.00086, 0.000892, 0.000922, 0.000948, 0.000971, 0.000992, 0.001003, 0.001004, 0.001006, 0.00102, 0.001054, 0.001111, 0.001182, 0.001268, 0.001367, 0.001481, 0.001599, 0.001725, 0.001867, 0.002037, 0.002246, 0.002486, 0.002751, 0.00305, 0.003397, 0.0038, 0.004239, 0.004706, 0.005234, 0.005854, 0.006601, 0.007451, 0.008385, 0.009434, 0.010629, 0.012002, 0.013569, 0.015305, 0.017192, 0.019208, 0.02133, 0.023489, 0.0257, 0.028068, 0.030696, 0.033688, 0.036904, 0.040275, 0.044013, 0.048326, 0.053427, 0.05939, 0.066073, 0.073366, 0.081158, 0.089339, 0.097593, 0.105994, 0.115015, 0.125131, 0.136815, 0.150191, 0.164944, 0.180886, 0.197834, 0.215601, 0.234658, 0.25513, 0.276308, 0.297485, 0.317953, 0.337425, 0.356374, 0.375228, 0.394416, 0.414369, 0.436572, 0.460741, 0.484644, 0.506047, 0.52272, 0.534237, 0.542088, 0.546908, 0.549333, 0.55, 0.55, 0.55, 1.0],
	),
)
