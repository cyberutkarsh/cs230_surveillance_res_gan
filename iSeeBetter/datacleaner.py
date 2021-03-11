
import os
import sys 

'''
Rename images in SPMCS so that frame-by-by name is im1.png, im2.png etc. 
'''


def reset_image_names(dir_images, base_folder, dryrun = True):
    new_file_names = []
    #pngCount = 0
    for count, image_name in enumerate(dir_images):
        if '.png' in image_name:
            new_image_name = image_name.replace('im', '')
            old_file_name = base_folder + '/' + image_name
            temp_file_name = base_folder + '/' + new_image_name
            if dryrun == False:
                os.rename(old_file_name, temp_file_name)
            new_file_names.append({
                "image_key": int(new_image_name.replace('.png', '')),
                "full_file_name": base_folder + '/' + new_image_name,
                "final_image_name":  base_folder + '/im' + new_image_name.replace('.png', '') + '.png'
            })
    new_file_names.sort()
    return new_file_names

def rename_images(dir_images):
    dir_images.sort(key=lambda x: x['image_key'])
    first_image_key = dir_images[0]['image_key']

    # Change file_name if first_index is not 0
    if first_image_key != 0:
        for key in range(len(dir_images)):
            current_image_key = dir_images[key]['image_key']
            dir_images[key]['final_image_name'] = dir_images[key]['final_image_name'].replace('im' + str(current_image_key) + '.png', 'im' + str(key) + '.png')
            dir_images[key]['image_key'] = key

    for image in dir_images:
        print(image)
        os.rename(image['full_file_name'], image['final_image_name'])

def main():
    SPMCS = os.listdir('./SPMCS')

    with open('./SPMCS/spcms_trainlist.txt') as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
    image_folders = [x.strip() for x in content] 

    image_folders = ['hk004_006/truth']

    for image_folder in image_folders:
        base_folder = './SPMCS/' + image_folder
        dir_images = os.listdir(base_folder)
        image_names = reset_image_names(dir_images, base_folder, False)
        print(image_names)
        rename_images(image_names)
    
    #print(image_folders)
    sys.exit()
    for filename in SPMCS:
        if ".txt" not in filename:
            dir_images = os.listdir('./SPMCS/' + filename)
            dir_images.sort()

            pngCount = 0
            for count, image_name in enumerate(dir_images):
                if '.png' in image_name:
                    os.rename('./SPMCS/' + filename + '/' + image_name, './SPMCS/' + filename + '/im' + str(pngCount) + '.png')
                    # print(pngCount, image_name)
                    pngCount += 1
                    
            # print(filename)
            # sys.exit()

if __name__ == "__main__":
    main()
