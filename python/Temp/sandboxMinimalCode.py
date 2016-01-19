x = "VFX_Plates_Cam_9624_CineF27_FPS1000.0001.jpg"

splitted =  x.split(".")
currentFrame = str(10)
splitted[1] = currentFrame.zfill(4)
print splitted

n = "4"
print n.zfill(4)


r = ['VFX_Plates_Cam_9624_CineF27_FPS1000', '0038', 'jpg']
print ".".join(r)