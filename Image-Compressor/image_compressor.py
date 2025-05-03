try:
################# Modules #######################
    from PIL import Image, ImageEnhance         #
    import pyfiglet                             #
    from datetime import datetime               #
    import sys                                  #
    import time                                 #
#################################################
    pf = pyfiglet.figlet_format("IMAGE COMPRESSOR")
    print(pf,"\n version 1.0")
    print()
    print('''
**********************************
* ------------------------------ *
* |Created by Mr. Susanta Banik| *
* ------------------------------ *
**********************************
''')
    print("************************")
    print("!General Instructions!")
    print("************************")
    print("****************************************************************************************************************")
    print("1. Enter the Image name correctly(eg.:photo.jpg)!")
    print("2. The image must be present in the "'original-img'" folder!")
    print("3. Compressed image is always less than 50KB!")
    print("4. You can also change the format(.jpg, .jpeg, .png and many more), converting to pdf is also acceptable!")
    print("****************************************************************************************************************")
    print()
    try: 
       img0=input("[+]Enter the image name(properly) that you want to compress: ")
       img='C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/original-img/'+img0       # Full folder Path
       img1= Image.open(img)
    except FileNotFoundError:
        print()
        print("-----------------------------------------------------------------------------------------------------------")
        print("[-]Something Went Wrong!")
        print("[?]Check either the image is present or not!")
        print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
        sys.exit()   
    print()
    q=input("[+]Do you want to set maximum size(initially 250X250)(yes/no): ")
    if q=="yes":
        print("[?]Image size might be more than 50 or 100KB based on original size, for less than 50kB it is recommanded to set it as initial or less!")
        print()
        x=int(input("[+]Enter the max width: "))
        y=int(input("[+]Enter the max height: "))
        print()
    else:
        x=250
        y=250
    MAX_SIZE=(x,y)
    img1.thumbnail(MAX_SIZE)
    enhancer1=ImageEnhance.Sharpness(img1)
    enhancer1.enhance(3.5).save("C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/temp-images/sharp-image.jpg")
    img2= Image.open('C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/temp-images/sharp-image.jpg')
    enhancer2=ImageEnhance.Color(img2)
    enhancer2.enhance(1.2).save("C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/temp-images/color-image.jpg")
    img3= Image.open('C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/temp-images/color-image.jpg')
    enhancer3=ImageEnhance.Brightness(img3)
    enhancer3.enhance(1.1).save("C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/temp-images/bright-image.jpg")
    img4= Image.open('C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/temp-images/bright-image.jpg')
    enhancer4=ImageEnhance.Contrast(img4)
    q2=input("[+]Do you want to change the name and format of your photo(initially Photo.jpg)(yes/no): ")
    if q2=="yes":
        name=input("[+]Enter the name with extension(eg.:Photo.jpg or Image.png or Photo.pdf): ")
        print()
        print("[?]Image is processing......")
        time.sleep(10)
        print()
    else:
        name="Photo.jpg"
        print()
        print("[?]Image is processing......")
    cimg="C:/Users/hp/OneDrive/Desktop/pyworks/Image-Compressor/final-image/"+name    
    enhancer4.enhance(1.1).save(cimg)
    print()
    print("****************************************** :Final Result: *******************************************************")
    print()
    print("[*]"+name,"saved succesfully into final-image folder")
    print()
    print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
    print("*****************************************************************************************************************")
except Exception and KeyboardInterrupt:
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("[-]Something Went Wrong!")
    print("[-]Exited at:",str(datetime.now().strftime("%I:%M %p")),"On",str(datetime.now().strftime("%d %B %Y, %A")))
    sys.exit()
##########################################################################################################################################################    
