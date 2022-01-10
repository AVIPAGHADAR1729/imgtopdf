

from PIL import Image
import time
import sys

def get_images_and_convert(*args):
    print(args)
    first_page = Image.open(args[0])
    pdf = first_page.convert('RGB')
    try:
        pdf.save(f'./{time.time()}_final_merged.pdf',save_all=True,append_images=[ Image.open(img).convert('RGB') for img in args[1:] ])
        print('Ok Done...')
    except FileExistError as FEE:
        print(FEE)
    finally:
        pdf.close()

##images = ('1.png','2.png','3.png')
##get_images_and_convert(*images)


# print(sys.argv)













##img = Image.open(path_list[0])
##			print('step0')
##			img = img.convert('RGB')
##			data = []
##			print('step1')
##
##			for x in path_list[1:]:
##				data.append(Image.open(x).convert('RGB'))
##
##			print('step2')
##
##			output = str(random.randint(100, 9000)) + '_out.pdf'
##
##			img.save('./response/'+output,'PDF',save_all=True,append_images=data)
##			img.close()
