import os
import shutil


VOC2012_trainval =  '/public/home/lcc-dx03/VOCdevkit/VOC2012/ImageSets/Main/car_trainval.txt'
# VOC2012_test =      'VOCdevkit/VOC2012/ImageSets/Main/person_test.txt'

VOC2012_label =     '/public/home/lcc-dx03/VOCdevkit/VOC2012/ImageSets/Main/'

VOC2012_images =        '/public/home/lcc-dx03/VOCdevkit/VOC2012/JPEGImages'
VOC2012_annotations =   '/public/home/lcc-dx03/VOCdevkit/VOC2012/Annotations'

FOLDER_TO_DELETE = ['VOCdevkit/VOC2012/SegmentationClass', 'VOCdevkit/VOC2012/SegmentationObject', 'VOCdevkit/VOC2012/ImageSets/Layout', 'VOCdevkit/VOC2012/ImageSets/Segmentation','VOCdevkit/VOC2012/ImageSets/Action']


train_person_index = []
# test_person_index = []

def rm_unnecessary_files():
    k = 0
    for file in FOLDER_TO_DELETE:
        if os.path.exists(file):
            shutil.rmtree(file)
    for file in os.listdir(VOC2012_label):
        if 'car' not in file:
            k = 1
        elif 'person' not in file:
            k = 1
        elif 'bus' not in file:
            k = 1
        else:
            k = 0
        if k == 1:
            os.remove(os.path.join(VOC2012_label, file))
    print('[0] remove unnecessary files done')

def get_index(dataset_path):
    person_index = []
    with open(dataset_path,'r') as f:
        line = f.readline()
        while line:
            if line[-3] != '-':
                index = line.split(' ')[0]
                if index not in person_index:
                    person_index.append(index)
            line = f.readline()
        f.close
    person_index.sort()
    print('[1] extract pics: %d'%(len(person_index)))
    return person_index


def write_txt(person_index, label_path):
    with open(os.path.join(VOC2012_label, label_path),'w') as f:
        for index in person_index:
            line = index + '\n'
            f.write(line)
    f.close
    print('    write labels into txt finished')


if __name__ == '__main__':
    rm_unnecessary_files()
    train_person_index = get_index(VOC2012_trainval)
    write_txt(train_person_index, 'train.txt')
    print('[2] All is done!')