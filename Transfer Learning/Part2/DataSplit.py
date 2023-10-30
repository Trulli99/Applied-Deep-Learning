fich_ts = open("data/KITTI/testing.txt", "w")
fich_tr = open("data/KITTI/training.txt", "w")

split_train = 0.8
split_test = 1 - split_train
n_imgs = 500

for i in range(int (n_imgs*split_train)):
    num = str(i)
    fich_tr.write("KITTI_dataset/Imgs/"+ num.zfill(6) +".png\n")

fich_tr.close()

for i in range(int(n_imgs*split_test)):
    num = str(i+int (n_imgs*split_train))
    fich_ts.write("KITTI_dataset/Imgs/"+ num.zfill(6) +".png\n")
    
fich_ts.close()