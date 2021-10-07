from PIL import Image
def func1():
    print("The library is loaded correctly.")
    backop = input("Which background would you like? Choices are: \n Beach \n Sunset \n Desert \n Earth \n Field \n Forest \n SnowsCape \n What do you choose? ")
    if(backop.lower() == "beach"):
        back_img = "beach.jpg"
    elif(backop.lower() == "sunset"):
        back_img = "sunset.jpg"
    elif(backop.lower() == "desert"):
        back_img = "desert.jpg"
    elif(backop.lower() == "earth"):
        back_img = "earth.jpg"
    elif(backop.lower() == "field"):
        back_img = "field.jpg"
    elif(backop.lower() == "forest"):
        back_img = "forest.jpg"
    elif(backop.lower() == "snowscape"):
        back_img = "snowscape.jpg"
    else:
        back_img = "beach.jpg"

    frontop = input("What do you want as the subject? choices are: \n Boat \n Cactus \n Cat \n Small Cat \n Harvester \n Hiker \n Penguin \n Spaceshuttle \n What do you choose? ")
    if(frontop.lower() == "boat"):
        front_img = "boat.jpg"
    elif(frontop.lower() == "cactus"):
        front_img = "cactus.jpg"
    elif(frontop.lower() == "cat"):
        front_img = "cat.jpg"
    elif(frontop.lower() == "small cat"):
        front_img = "cat_small.jpg"
    elif(frontop.lower() == "harvester"):
        front_img = "harvester.jpg"
    elif(frontop.lower() == "hiker"):
        front_img = "hiker.jpg"
    elif(frontop.lower() == "penguin"):
        front_img = "penguin.jpg"
    elif(frontop.lower() == "spaceshuttle"):
        front_img = "spaceshuttle.jpg"
    else:
        front_img = "penguin.jpg"

    print("Creating Image")
    yH = 0
    xW = 0
    bFile = back_img
    front_image = front_img
    image_front = Image.open(front_image)
    image_background = Image.open(bFile)
    width, height = image_background.size
    pixels_original = image_front.load()
    pixels2 = image_background.load()
    for yH in range(0, height):
        for xW in range (0, width):
            r, g, b = pixels_original[xW, yH]
            if(g > 100 and r < 100 and b < 100):
                r2, g2, b2 = pixels2[xW, yH]
                pixels_original[xW, yH] = (r2, g2, b2)

    image_front.show()
    #image_original = Image.open("beach.jpg")
    image_front.save("the_new_image.jpg")


    
#driving

func1()
#image_front = Image.open(front_image)
a = input("Would you like to try remaking the image? y or n\n")
if a == "y":
    func1()

        
