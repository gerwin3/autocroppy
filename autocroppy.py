import sys
import os

import cv2
import tkMessageBox

from autocropper import AutoCropper

# changing this to True will cause the program to show the
# original and cropped version and ask if you want to store
# it or not
INTERACTIVE_MODE = False

def show_picture(name, img):
    
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 800, 600)
    cv2.imshow(name, img)

def main():

    # you can provide both the input and output directory
    # yourself, by default dir_in will be the current dir
    # and dir_out will be <current_dir>/out/
    if len(sys.argv) == 1:
        dir_in = os.path.abspath('.')
        dir_out = os.path.join(os.path.abspath('.'), "out\\")
    elif len(sys.argv) == 2:
        dir_in = os.path.abspath(sys.argv[1])
        dir_out = os.path.join(os.path.abspath('.'), "out\\")
    elif len(sys.argv) == 2:
        dir_in = os.path.abspath(sys.argv[1])
        dir_out = os.path.abspath(sys.argv[2])
    else:
        print "usage: gvdl-autocrop [input-dir] [output-dir]"
        return 1
    
    # make dir_out if it doesn't exist yet ...
    if not os.path.exists(dir_out):
        os.mkdir(dir_out)

    # loop through *.jpg files in the current direcotry and
    # call process_image on them
    for f in os.listdir(dir_in):
        if os.path.isfile(f) and f[-4:] == ".jpg":
            
            original = cv2.imread(f, cv2.IMREAD_COLOR)
            if original == None:
                continue
            
            cropper = AutoCropper(original)
            cropper.safety_margin = 32
            
            crop = cropper.autocrop()

            # calculate how much we've deleted, and print some output
            o_area = original.shape[0] * original.shape[1]
            c_area = crop.shape[0] * crop.shape[1]
            
            factor_removed = 1.0 - (float(c_area) / float(o_area))
            
            print " >> cropped away " + str(factor_removed*100) + "% from " + os.path.basename(f)
            
            # if we're running interactive, show the original and the
            # cropped version and ask whether we should store it, otherwise
            # simply store to the out_dir
            if INTERACTIVE_MODE:
                show_picture("Before", original)
                show_picture("After", crop)
            
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            
            # ask whether to store...
            if INTERACTIVE_MODE:
                if tkMessageBox.askyesno("So?", "Store this image in the output directory?"):
                    cv2.imwrite(os.path.join(dir_out, os.path.basename(f)), crop)
            else:
                cv2.imwrite(os.path.join(dir_out, os.path.basename(f)), crop)
        
# entrance point
if __name__ == "__main__":
    sys.exit(main())

