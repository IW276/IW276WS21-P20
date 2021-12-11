import scipy.io
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(""):
    f.extend(filenames)
    print(str(f))
    break

# file = open("0001_c1s1_001051_00_good.mat", "r")

# print(file.read())

# mat = scipy.io.loadmat("F:\\AS_Labor\\IW276WS21-P20\\src\\0001_c1s1_001051_00_good.mat")
mat = scipy.io.loadmat(
    "F:\\AS_Labor\\IW276WS21-P20\\reid-data\\market1501\\Market-1501-v15.09.15\\gt_query\\0001_c3s1_000551_00_good.mat"
)
mat2 = scipy.io.loadmat(
    "F:\\AS_Labor\\IW276WS21-P20\\reid-data\\market1501\\Market-1501-v15.09.15\\gt_query\\0001_c3s1_000551_00_junk.mat"
)

print(str(mat))
print(str(mat2))

