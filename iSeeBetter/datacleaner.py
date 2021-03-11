
import os
import sys 

'''
Rename images in SPMCS so that frame-by-by name is im1.png, im2.png etc. 
'''


def reset_image_names(dir_images, base_folder, dryrun = True):
    new_file_names = []
    
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
        
        os.rename(image['full_file_name'], image['final_image_name'])

def main():
    SPMCS = os.listdir('./SPMCS')

    with open('./SPMCS/spcms_trainlist.txt') as f:
        content = f.readlines()
        
    image_folders = [x.strip() for x in content] 

    # Uncommend if you want to debug specific folder
    # image_folders = ['PRVTG_008/truth']

    for image_folder in image_folders:
        print('STARTED', image_folder)
        base_folder = './SPMCS/' + image_folder
        dir_images = os.listdir(base_folder)
        image_names = reset_image_names(dir_images, base_folder, False)
        
        rename_images(image_names)
        
    
    sys.exit()

if __name__ == "__main__":
    main()
