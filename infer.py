import torch
import cv2
from pathlib import Path

# 参数
WEIGHTS = r'runs/train/exp/weights/best.pt'    # 权重路径
SOURCE = r'E:\pycharm\Projects\yolov5\test'    # 数据路径
SAVE_DIR = r'runs/detect/result'    # 保存路径

# 加载模型
print('Loading model.....')
model = torch.hub.load(r'E:\pycharm\Projects\yolov5',
        'custom',
        path=WEIGHTS,
        source='local')

model.conf = 0.49   # 置信度阈值
model.iou = 0.45    # IoU阈值

# 创建保存目录
save_dir = Path(SAVE_DIR)
save_dir.mkdir(parents=True, exist_ok=True)

# 推理
img_paths = list(Path(SOURCE).glob('*.jpg'))
for img_path in img_paths:
        print(f'Detecting: {img_path.name}')
        results = model(str(img_path))

        # 保存图片
        results.save(save_dir=str(save_dir))

        # 读取检测数据
        boxes = results.xyxy[0]   # boxes是一个二维结构(n, 6)，n表示检测到的目标数量，每个目标有6个固定值
        for box in boxes:
                x1, y1, x2, y2, conf, cla = box.tolist()    #把每个目标的6个固定值转为list
                print(f'box: {x1: .1f},{y1: 1f},{x2: 1f},{y2: 1f}, conf:{conf}')

