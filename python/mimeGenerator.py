import settings

class MimeGenerator(object):
	def __init__(self, parent):
		self.parent = parent
		pass

	def itemDragged(self, itemID ):
		print settings.pathCache[self.parent.currentCategory][str(itemID)]



	def generateNukeTCL(self):
		command = ""
		command += """Read {
			inputs 0
 			file C:/Users/PC/Desktop/Projects/Elementsbrowser/ElementsBrowserPY/python/Categories/Cloth/A002C002_140913_FPS120/Thumbnails/A002C002_140913_FPS120.1001.jpg}"""
 		return command


# m = MimeGenerator()
# print m.generateNukeTCL()
# QString Thumbnail::generateNukeTCL(){

#     return QString("Read {inputs 0 file " + this->pathToSource + "" + this->fileName + ".####.exr" + "\n" +
#                    " proxy " + this->pathToProxy + this->fileName+ ".####.jpg"+               "\n" +
#                     "format " + "\"" + QString::number(this->imageWidth) + " " + QString::number(this->imageHeight) + "\""+               "\n" +
#                    " proxy_format " + "\"" + QString::number(this->imageWidth) + " " + QString::number(this->imageHeight) + "\""+               "\n" +
#                    " first " + QString::number(this->startFrame) + "\n" +
#                    " last  " + QString::number(this->startFrame + this->NumOfFrames -1)+ "\n" +
#                    " origfirst " + QString::number(this->startFrame) + "\n" +
#                    " origlast  " + (QString::number(this->startFrame + this->NumOfFrames-1))+ "\n" +
#                    " label " + "\"Elementsbrowser Id #" +  QString::number(this->Id)+ "\"" + "\n" +


#                    "}" );

# }
