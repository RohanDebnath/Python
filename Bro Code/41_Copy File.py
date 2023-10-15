#copyfile()= copy contents of a file
#copy()=     copyfile()+ permission mode + destination can be in a directory
#copy2()=    copy()+ copy metadata (file's creation and modification timed)

import shutil
shutil.copyfile("C:\\Users\\USER\\Desktop\\textfile.txt","C:\\Users\\USER\\Desktop\\test.txt")