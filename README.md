# Meet Eobard, a split 34 key ortholinear keyboard.
Current Hardware Revision: 0.2.8

<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Keyboard.jpg" width="75%">

## Project Description
Eobard is an ortholinear 34 key split keyboard made for my personal needs. Inspired by the [Ferris](https://github.com/pierrechevalier83/ferris).

The columns are spaced out vertically so as to provide the most comfortable typing experience for my hand size. It is designed to be cheap to manufacture and simple to assemble. The single PCB is dual sided, only having to be flipped around for assembly of the other side.

<details>
<summary>Hardware Tasks</summary>

- [x] Design Layout. 
- [x] Design PCB & Plate.
- [x] Generate Gerbers.
- [x] Build Prototype.
- [ ] Write Build Guide with images.
- [x] Change 5th Column Spacing to a more comfortable distance.
- [ ] Make the right side's BOOTSEL button more accessible after soldering.
- [x] Get permission to use the BTW creature in silkscreen.
- [x] Change Placement of TRRS footprints on PCB.
- [x] Move Thumb Keys to Rows 4 and 5.
- [x] Make board diodeless.
- [ ] Release First Version.
</details>

<details>
<summary>Software Tasks</summary>

- [x] Write US English Base Layout.
- [x] Write EU Portuguese Base Layout.
</details>

## Images
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Front%20and%20Back.jpg" width="75%">
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Board-Images/eobard_front.jpg" width="75%">
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Board-Images/eobard_back.jpg" width="75%">
<img src="https://github.com/viniciusbrit/eobard/blob/54abefa3f9322f3dde9a3adc79b1acc81ec4291c/Images/Plate-Images/eobard-plate_front.jpg" width="75%">

## Bill of materials
* Raspberry Pi Pico [x2]
* [PJ-320A 3.5mm Audio Jack [x2]](https://www.lcsc.com/product-detail/Audio-Connectors_Hong-Cheng-HC-PJ-320A_C7501806.html)
* Cherry MX Style Switches [x34]
* 4mm M2 Standoff [x9]
* 3mm M2 Screws [x18]
* 01x20 2.54mm Standard Male Pin Headers [x4] [If Pico doesn't have them pre-soldered]

## Ordering PCBs
Dragging and dropping the provided Gerber zips onto JLCPCB or other manufacturer's websites should work just fine. Make sure the plate PCB is 1mm thick and the main pcb is 1.6mm thick.
