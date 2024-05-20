
from opt import opt

from utils.comm import generate_model

save_path = "cli"
import torch.nn.functional as F

import os
from utils.transform import *

from torchvision import transforms
from torchvision.utils import save_image
from tqdm import tqdm

source_path = '../data/train/masks'
transform = transforms.Compose([
                   transforms.Resize((352, 352)),
                   #RandomHorizontalFlip(),
                   #RandomVerticalFlip(),
                   #RandomRotation(90),
                   #RandomZoom((0.9, 1.1)),
                   #Translation(10),
                   #RandomCrop((224, 224)),
                   transforms.ToTensor(),

               ])
def test():
    list = os.listdir('./edge_test/images')
    model = generate_model(opt)
    model.cpu()
    for img_name in tqdm(list):
        img = Image.open('./edge_test/images/'+img_name).convert('RGB')

        img = transform(img)
        img = img.cpu()
        img = img.unsqueeze(0)
        output, pr1, pr2, pr3, pr4, edge1, edge0 = model(img)
        # edge = F.upsample(edge0, size=(320, 320), mode='bilinear', align_corners=False)
        save_image(edge1, "./edge_result/{}".format(img_name))


if __name__ == '__main__':
    print('--- PolypSeg Test---')
    test()

    print('Done')
