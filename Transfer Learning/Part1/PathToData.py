fich = open("YOLO/data/KITTI/dataset.txt", "w")

n_imagens = 500

for i in range(int(n_imagens)):
    num = str(i)
    fich.write("YOLO/KITTI_dataset/Imgs/"+ num.zfill(6) +".png\n")

fich.close()
