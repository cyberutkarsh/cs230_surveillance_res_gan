
import os
import sys 

'''
Renmae images in SPMCS, so that 
'''
def main():
    SPMCS = os.listdir('./SPMCS')
    for filename in SPMCS:
        if ".txt" not in filename:
            dir_images = os.listdir('./SPMCS/' + filename)
            dir_images.sort()
            for count, image_name in enumerate(dir_images):
                if '.png' in image_name:
                    os.rename('./SPMCS/' + filename + '/' + image_name, './SPMCS/' + filename + '/im' + str(count) + '.png')
            # print(filename)
            # sys.exit()

if __name__ == "__main__":
    main()
