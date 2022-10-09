from PIL import Image
import os

# filein: 输入图片路径
# fileout: 输出图片路径
# width: 输出图片宽度
# height:输出图片高度
# xtype:输出图片类型（png, gif, jpeg...）
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
  out.save(fileout)
def Image_PreProcessing(filein,fileout,width,height):
  	# 待处理图片存储路径	
	im = Image.open(filein)
	# Resize图片大小，入口参数为一个tuple，新的图片大小
	imBackground = im.resize((width,height))
	#处理后的图片的存储路径，以及存储格式
	imBackground.save(fileout,'JPEG')
if __name__ == '__main__':
  fi=[]
  for root,dirs,files in os.walk('./'):
    for file in files:
      fi.append(file)
  fi.remove('change.py')
  width=224
  height=224
  for f in fi:
    Image_PreProcessing(f,f,width, height)
    