import sys
sys.path.insert(0, '/media/caimao/项目/caffe/python')
import caffe
import cv2
import pdb
import numpy as np

# 定义网络的路径

proto_file = 'modnet_sim_sigmoid.prototxt'
# proto_file = 'modnet_sim_argmax.prototxt'

model_file = 'modnet_sim.caffemodel'


# 创建网络实例

net = caffe.Net(proto_file, model_file, caffe.TEST)

img = cv2.imread('test2.jpg')
img_ori = img.copy()
img_ori_h = img_ori.shape[0]
img_ori_w = img_ori.shape[1]

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(384,384))

img = (img - 127.5) / 127.5 

img = np.transpose(img,(2,0,1))
img = img[np.newaxis,:,:,:]

net.blobs['input'].data[...] = img
output = net.forward()['output'].squeeze()

output = cv2.resize(output,(img_ori_w,img_ori_h))
# img_ori[output == 0] = np.array([219,142,67])
img_ori[output < 0.5] = np.array([219,142,67])
cv2.imwrite('result_sigmoid.jpg',img_ori)