# Meet Eobard, a split 34 key ortholinear keyboard.
Current Hardware Revision: 0.2.8 

<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Keyboard.jpg" width="75%">

## Project Description
Eobard is an ortholinear 34 key split keyboard made for my personal needs. Inspired by the [Ferris](https://github.com/pierrechevalier83/ferris).

The columns are spaced out vertically so as to provide the most comfortable typing experience for my hand size. It is designed to be cheap to manufacture and simple to assemble. The single PCB is is dual sided, only having to be flipped around for assembly of the other side.

<details>
<summary>Hardware Tasks</summary>
## List of Eobard Hardware Design Tasks
- [x] Design Layout. 
- [x] Design PCB & Plate.
- [x] Generate Gerbers.
- [x] Build Prototype.
- [ ] Write Build Guide with images.
- [ ] Change 5th Column Spacing to a more comfortable distance.
- [ ] Make the left side's BOOTSEL button more accessible after soldering.
- [ ] Add proper spaces for rubber feet.
- [ ] Change Placement of TRRS footprints on PCB.
</details>

<details>
<summary>Software Tasks</summary>
- [x] Write US English Layout.
- [x] Write EU Portuguese Layout.
- [ ] Get OLED displays working.
- [ ] Write OLED behaviour.
</details>

## Images
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Front%20and%20Back.jpg" width="75%">
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Board-Images/eobard_front.jpg" width="75%">
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Board-Images/eobard_back.jpg" width="75%">
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Plate-Images/eobard-plate_front.jpg" width="75%">

## Bill of materials
* Raspberry Pi Pico [x2]
* [PJ-320A 3.5mm Audio Jack [x2]](https://www.lcsc.com/product-detail/Audio-Connectors_Hong-Cheng-HC-PJ-320A_C7501806.html)
* [SSD1306 0.91" I2C OLED Display Module [x2]](https://pt.aliexpress.com/item/32672229793.html) [Optional] [Functionality Not Yet Implemented]
* [1N4148 THT Diodes [x34]](https://www.lcsc.com/product-detail/Switching-Diode_LGE-1N4148_C402212.html)
* Cherry MX Style Switches [x34]
* 4mm M2 Standoff [x9]
* 3mm M2 Screw [x18]
* 01x04 2.54mm Female Pin Headers [x2] [For OLED Displays]
* 01x20 2.54 Standard Male Pin Headers [x4] [If Pico doesn't have them pre-soldered]

## Ordering PCBs
Dragging and dropping the provided Gerber zips onto JLCPCB or other manufacturer's websites should work just fine. Make sure the plate PCB is 1mm thick and the main pcb is 1.6mm thick.
