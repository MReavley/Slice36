# ThinSlice36 Minimalist Split Keyboard

Modification of the Slice36 for thinness. 

## Modifications from upstream:

- Low-profile switches (choc v1)
- Choc spacing
- Reversible PCB, designed around 0805 smd components to be hand-solderable or using an assembly service.
- Built around the Seeeduino Xiao RP2040(hooray USB-C), using KMK.  
- No plate

## BOM
- Seeeduino Xiao RP2040 x2
- 1N4148WS Diodes (SOD-323) x36
- PJ320D TRRS jacks x2
- 0805 10k resistors x6 (additional footprints R4-R7 for I2C communication for splits, may not be required)
- Kailh Choc v1 style switches x36
- Keycaps x36
- TRRS cable  

## Things to note if you want to build one:

- IMPORTANT: The xiao on the right half (master) is to be soldered with the LED/chip facing up, and the left half (slave) upside down, so that the pinout still matches the flipped PCB.
- Upstream uses 8mm rubber feet that are 1.5mm tall which are just about tall enough, but taller rubber feet might be better.
- TRRS jacks for the split are connected to the I2C pins on the Xiao board. Since KMK uses UART for split communications, I used PIO on the RP2040 to change those pins to UART, but I don't know what your options are on the SAMD21 version if you wish to use UART on those.
- Upstream prototype found that the SAMD21 version of the Xiao required external pullups on the I2C lines and added those to this board, but has not tested if they are necessary yet. Currently using 10k resistors (to simplify BOM), and it is working fine.
