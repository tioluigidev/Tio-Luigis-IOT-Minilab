# USB Power Module

## Description

![PSU Module](images/panels/module-usbpower.jpg)

This module is intended to power up the devices with USB power cords. These devices may be inside the minilab rack mount or outside (on a workbench, for example). I did´t built it from stratch. Instead, I used an USB charger with 4 ports and an extra port with Quick Charge 3.0 standard capabilities.

## Schematics

![USB Power Module Schematics](images/schematics/module-usbpower.jpg)
Important: It´s necessary to connect any GND point in the Charger to the GND terminal bar at the rear of the rack.

## 3D Printed Parts

To make the 3d printed parts, I used an Creality Ender 3 similar 3d printer. Some parts I printed with 0.8mm nozzle, just for speed gain (where aesthetics were not so important). For all the other parts, I used 0.4mm nozzle. The original editable Blender files are also included in the "3dprint" directory.

Caption|File|Prints|Nozzle|Supports|Description|
|---|---|---|---|---|---|
| 1|[usbpower.base.stl](./3dprint/usbpower/usbpower.base.stl)|1|0.8|No|Module base.|
| 2|[usbpower.innersupport.left.stl](./3dprint/usbpower/usbpower.innersupport.left.stl)|1|0.4|Yes|Left inner support for the usb charger circuit.|
| 3|[usbpower.innersupport.right.stl](./3dprint/usbpower/usbpower.innersupport.right.stl)|1|0.4|Yes|Right inner support for the usb charger circuit.|
| 4|[usbpower.panel.front.stl](./3dprint/usbpower/usbpower.panel.front.stl) |1|0.8|No|Front panel for the module.|
| 5|[usbpower.panel.powerpanel.stl](./3dprint/usbpower/usbpower.panel.powerpanel.stl)|1|0.4|No|Power switch protector.|
| 6|[usbpower.panel.handler.stl](./3dprint/usbpower/usbpower.panel.handler.stl)|2|0.4|Maybe|Module handlers.|

![3D Printed Parts for PSU Module](images/3dprint/module-usbpower.jpg)

## Paper Printed Parts

I used inkjet printer and an off-white 180g/m2 paper to make the front panel of the modules. In Brazil, this paper is known as "Color Plus 180g Marfim". To create these files, I used a software called "Graphics", that works on Mac. The original editable Graphics file for each print is in the "print" directory.

|File|Description|
|---|---|
|[print.usbpower.panel.pdf](./print/print.usbpower.panel.pdf)|USB Power Module front panel.|

## Shopping List

Qty|Description|
|---|---|
|  1| USB Charger. I found mine in [this link](https://pt.aliexpress.com/item/32979578903.html), but I don´t know if "Tongdaytech" is the brand or the name of the shop. |
| 1 |Margirius lever microswitch bipolar with 2 positions (on/off).|
| 1 meter|0.30mm black wire.|
| 5 ~ 10|Nylon cable ties.|
| 10|Allen Bolt M5x6 Cylindrical Head.|
| 4 |Allen Bolt M5x6 Flat Head.|
| 4 |Hammer Nut M5.|
| 1 |Thick paper sheet (if you want to print the panel).|
| ~ 130g | PLA 3D print filament.|

## Nuts and Bolts

Picture|Description|
|---|---|
|![PSU Module](images/nutsandbolts/nutsandbolts-01.jpg)|Allen Bolt M5x6 Cylindrical Head (5mm on diameter, 6mm on length)|
|![PSU Module](images/nutsandbolts/nutsandbolts-02.jpg)|Allen Bolt M5x6 Flat Head (5mm on diameter, 6mm on length)|
|![PSU Module](images/nutsandbolts/nutsandbolts-03.jpg)|Hammer Nut M5 (for 5mm diameter bolts)|

## Pictures

![USB Power Module](images/pictures/module-usbpower-001.jpg)

![USB Power Module (whole)](images/pictures/module-usbpower-002.jpg)

![USB Power Module (inside right)](images/pictures/module-usbpower-003.jpg)

![USB Power Module (inside left)](images/pictures/module-usbpower-004.jpg)

![USB Power Charger](images/pictures/module-usbpower-005.jpg)

