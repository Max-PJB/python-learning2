'''
Input:
p_x=[x1,y1,w1,h1]
p_y=[x2,y2,w2,h2]

'''


def IoU(p_x, p_y):
    area_x = p_x[2] * p_x[3]
    area_y = p_y[2] * p_y[3]

    x_tl = max(p_x[0], p_y[0])
    y_tl = max(p_x[1], p_y[1])
    x_br = min(p_x[0] + p_x[2], p_y[0] + p_y[2])
    y_br = min(p_x[1] + p_x[3], p_y[1] + p_y[3])

    inter_w = max(x_br - x_tl, 0)  # 与 0 比较是为了防止两个不相交的情况
    inter_h = max(y_br - y_tl, 0)  # 与 0 比较是为了防止两个不相交的情况

    inter_area = inter_h * inter_w

    return inter_area * 1.0 / (area_x + area_y - inter_area)


import numpy as np

'''
input:
dets=[[x1,y1,x2,y2],[x1,y1,x2,y2],...] 
thresh: float
'''


def nms(dets, thresh):
    # 以下 5 个都是多维的数组
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    # 用数组存储所有 box 的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    # 将数组的类别分数从大到小排序，并得到它们排序后的索引顺序
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

        inds = np.where(ovr <= thresh)[0]  # np.where() 直接将小于阈值的去除了，返回 tuple（[index1,index2,...],）
        order = order[inds + 1]

    return keep


def bbox_iou(bbox_a, bbox_b):
    """
	计算两组方框之间的IOU值。

	bbox_a：一个numpy.ndarray型二维数组，shape为（N，4），N代表bbox_a包含的方框个数
	bbox_b: 一个numpy.ndarray型二维数组，shape为（k，4），K代表bbox_b包含的方框个数
	4表示每个方框的坐标，按顺序依次表示y_min,x_min,y_max,x_max
	min代表左上角，max代表右下角，在图片中，左上角代表坐标原点，正方向为下、右。

	此函数需要计算的就是bbox_a中的每个方框与bbox_b中的每个方框的IOU值，所以最后返回的数组shape为（N,K）

Calculate the Intersection of Unions (IoUs) between bounding boxes.

    IoU is calculated as a ratio of area of the intersection
    and area of the union.

    This function accepts both :obj:`numpy.ndarray` and :obj:`cupy.ndarray` as
    inputs. Please note that both :obj:`bbox_a` and :obj:`bbox_b` need to be
    same type.
    The output is same type as the type of the inputs.

    Args:
        bbox_a (array): An array whose shape is :math:`(N, 4)`.
            :math:`N` is the number of bounding boxes.
            The dtype should be :obj:`numpy.float32`.
        bbox_b (array): An array similar to :obj:`bbox_a`,
            whose shape is :math:`(K, 4)`.
            The dtype should be :obj:`numpy.float32`.

    Returns:
        array:
        An array whose shape is :math:`(N, K)`. \
        An element at index :math:`(n, k)` contains IoUs between \
        :math:`n` th bounding box in :obj:`bbox_a` and :math:`k` th bounding \
        box in :obj:`bbox_b`.

    """
    if bbox_a.shape[1] != 4 or bbox_b.shape[1] != 4:
        raise IndexError

    # top left
    tl = np.maximum(bbox_a[:, None, :2], bbox_b[:, :2])
    # bottom right
    br = np.minimum(bbox_a[:, None, 2:], bbox_b[:, 2:])

    area_i = np.prod(br - tl, axis=2) * (tl < br).all(axis=2)
    area_a = np.prod(bbox_a[:, 2:] - bbox_a[:, :2], axis=1)
    area_b = np.prod(bbox_b[:, 2:] - bbox_b[:, :2], axis=1)
    return area_i / (area_a[:, None] + area_b - area_i)

# 除此之外，还可以直接调用pytorch(>=1.2.0)、torchvision(>= 0.3)中封装好了的nms函数。
"""
from torchvision.ops import nms
keep = nms(boxes,scores,iou_threshold)  

#返回的keep表示为经过nms后保留下来的boxes的索引值，并且keep的中索引值是按照scores得分降序排列的
#len(keep) <= len(boxes)

#通过下列操作即可获取具体nms后的boxes
boxes = boxes[keep]

参数：
boxes (Tensor[N, 4])) – bounding boxes坐标. 格式：(x1, y1, x2, y2)

scores (Tensor[N]) – bounding boxes得分

iou_threshold (float) – IoU过滤阈值
"""
