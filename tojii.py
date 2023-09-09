from PIL import Image, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt

# pic = "original.jpg"

# with Image.open(pic) as doggo:
#     size = doggo.size
#     type = doggo.format
#     mode = doggo.mode
#     print(size)
#     print(type)
#     print(mode)

pict = 'toji.jpg'

with Image.open(pict) as toji:
    size = toji.size
    format = toji.format
    mode = toji.mode
    print(size)
    print(format)
    print(mode)

Imageop = Image.open(pict)
Imageop.show()



blurImage = Imageop.filter(ImageFilter.BLUR)
blurImage.show()
blurImage.save('blurredtoji.jpg')



rotateImage = Imageop.transpose(Image.ROTATE_90)
rotateImage.show()
rotateImage.save("up.jpg")



roImage = Imageop.rotate(90)
roImage.show()
roImage.save("90.jpg")



greyImage = Imageop.convert("L")
greyImage.show()
greyImage.save('gray.jpg')


mirrorImage = Imageop.transpose(Image.FLIP_LEFT_RIGHT)
mirrorImage.show()
mirrorImage.save("mirror.jpg")



contrastImage = ImageEnhance.Contrast(Imageop)
contrastImage = contrastImage.enhance(1.5)
contrastImage.show()
contrastImage.save("contr.jpg")



sharpenImage = Imageop.filter(ImageFilter.SHARPEN)
sharpenImage.show()
sharpenImage.save("sharpenedtoji.jpg")



smoothImage = Imageop.filter(ImageFilter.SMOOTH_MORE)
smoothImage.show()
smoothImage.save("smoothtoji.jpg")







image1 = Image.open("mirror.jpg") #blend images
image2 = Image.open("toji.jpg")

blend = Image.blend(image1,image2,alpha=0.5)
blend.show()
blend.save("blend.jpg")


imageCropped = image1.crop(box = (20,20,200,200)) #crop images
imageCropped.show()