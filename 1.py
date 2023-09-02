from PIL import Image

# pic = "original.jpg"

# with Image.open(pic) as doggo:
#     size = doggo.size
#     type = doggo.format
#     mode = doggo.mode
#     print(size)
#     print(type)
#     print(mode)

pict = 'mhh.png'

with Image.open(pict) as spiderman:
    size = spiderman.size
    format = spiderman.format
    mode = spiderman.mode
    print(size)
    print(format)
    print(mode)