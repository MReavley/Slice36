# Slice36 Minimalist Split Keyboard

![Picture of the Slice36](https://github.com/MReavley/Slice36/blob/main/Slice36%20Pictures/IMG_1024.JPG)

36 key ergo split keyboard, designed around the Seeeduino Xiao platform. Inspired by the Corne, Ferris, Ben Vallack's videos and countless hours of perusing reddit and kbd.news, but ultimately this has been done up from scratch largely as an exercise for myself. The layout was generated through experimentation with scale drawings on my ipad, although emphasis has been placed on aesthetics and compactness. 

## Features

-MX Spacing  
-Reversible PCB, designed around 0805 smd components to be hand-solderable or using an assembly service.  
-Built around the Seeeduino Xiao RP2040(hooray USB-C), using KMK.  
-Laser cut aluminium plate, secured by the soldered in switches for clean look without fasteners  

![Picture of the Slice36 and PCB](https://github.com/MReavley/Slice36/blob/main/Slice36%20Pictures/IMG_1029.JPG)

## BOM
-Seeeduino Xiao RP2040 x2  
-1N4148WS Diodes (SOD-323) x36  
-PJ320D TRRS jacks x2  
-0805 10k resistors x6   
-(additional footprints R4-R7 for I2C communication for splits, may not be required)  
-Cherry MX style switches x36  
-Plate x2   
-TRRS cable  

## Things to note if you want to build one:

-IMPORTANT: The xiao on the right half (master) is to be soldered with the LED/chip facing up, and the left half (slave) upside down, so that the pinout still matches the flipped PCB.  

-You can find the schematic, layout and gerbers in the repo, as well as a dxf file for the plate. I am currently working on a case for this and will add the stls and solidworks files once they are ready. 

-I use 8mm rubber feet that are 1.5mm tall which are just about tall enough, but I think taller rubber feet would be better.

-TRRS jacks for the split are connected to the I2C pins on the Xiao board. Since KMK uses UART for split communications, I used PIO on the RP2040 to change those pins to UART, but I don't know what your options are on the SAMD21 version if you wish to use UART on those.  

-From my first prototype, I found that the SAMD21 version of the Xiao required external pullups on the I2C lines, so I added those to this board, and I have not tested if they are necessary yet. Currently I am using 10k resistors (to simplify my BOM), and it is working fine.  

-The Xiao BLE version should also be compatible with this board, but I have not made any provisions for batteries on this version. In theory only minimal modifications would be necessary to get this going though.  

![Picture of the Slice36 and PCB](https://github.com/MReavley/Slice36/blob/main/Slice36%20Pictures/IMG_1027.JPG)
![Picture of the Slice36 and PCB](https://github.com/MReavley/Slice36/blob/main/Slice36%20Pictures/IMG_1011.JPG)
