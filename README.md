### MODNet ONNX转Caffe工程
mlu220只支持caffe量化加密，网上找了一大圈也没找到MODNet的onnx转caffe的工程，开源的onnx2caffe工程有些算子支持不全，没办法只能自己改了（难受)；
使用方法不多说了，看sh文件即可，转好的caffemodel也上传了，直接用也行，链接：链接: https://pan.baidu.com/s/1ufMDc0UIMmzT9p9UTl1Q-w?pwd=uq2k 提取码: uq2k；
注意：此工程只能用来转MODNet的caffe模型，想转其他模型可以自己动手改，重点改onnx2caffe目录下_operators.py；