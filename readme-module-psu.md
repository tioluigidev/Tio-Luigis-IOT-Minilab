# PSU Module



## Description

The PSU (Power Supply Unity) Module is responsible to power up all the system. The main power switch is a 6A circuit breaker. In my project, I used a circuit breaker with residual current protection, to prevent electrical shock. There is also a power meter with a double display, for voltage and current measuring. The main power line ends in a power strip, in my case with 4 electrical outlets.

Connected to this power strip, there is an ATX Power Supply. For this project I used a 250W retail model. This ATX PSU powers the 4 terminal bars at the rear part of the rack. These terminal bars are used to power all the small circuits and IOT devices that uses 3.3V, 5V and/or 12V power.

The ATX PSU also powers a Workbench Module, used to provide voltage to workbench projects and experiments. Connected to this module, there is the ATX Power Switch, that starts up the ATX PSU and a potentiometer for adustable voltage output, provided by the workbench module too. 

## Schematics

![PSU Module Schematics](images/schematics/schematics-psumodule.jpg)

## 3D Printed Parts

Caption|File|Prints|Nozzle|Supports|Description|
|---|---|---|---|---|---|
| 1|[psu.base.stl](./3dprint/psu/psu.base.stl)|1|0.8|No|Module base, wich supports the ATX PSU.|
| 2|[psu.cableguide.stl](./3dprint/psu/psu.cableguide.stl)|1|0.8|Maybe|Inner cable guide. I didn't use supports.|
| 3|[psu.circuitbreakersupport.stl](./3dprint/psu/psu.circuitbreakersupport.stl)|1|0.8|No|Circuit breaker support. Necessary to keep the circuit breaker in the correct position and tight attached to the front panel.|
| 4|[psu.potentiometersupport.stl](./3dprint/psu/psu.panel.potentiometersupport.stl) |1|0.4|Yes|Adjustable voltage potentiometer support. Necessary to keep the potentiometer in the correct position and tight attached to the front panel.|
| 5|[psu.panel.front.stl](./3dprint/psu/psu.panel.front.stl)                 |1|0.8|No|Front panel, where all other panel components are attached to.|
| 6|[psu.panel.modulecover1.stl](./3dprint/psu/psu.panel.modulecover1.stl)   |1|0.4|No|Workbench module base.|
| 7|[psu.panel.modulecover2.stl](./3dprint/psu/psu.panel.modulecover2.stl)   |1|0.4|No|Workbench module cover.|
| 8|[psu.panel.circuitbreakerpanel.stl](./3dprint/psu/psu.panel.circuitbreakerpanel.stl)|1|0.4|No|Circuit breaker front protector.|
| 9|[psu.panel.meterpanel.stl](./3dprint/psu/psu.panel.meterpanel.stl) |1|0.4|No|Power meter front base.|
|10|[psu.panel.handler.stl](./3dprint/psu/psu.panel.handler.stl)       |2|0.4|Maybe|Left and right module handler. I used supports.|


![3D Printed Parts for PSU Module](images/3dprinted/3dprint-psumodule.jpg)

## Paper Printed Parts

|File|Description|
|---|---|
| 1|xxx|
| 1|xxx|

## Shopping List

Qty|Description|
|---|---|
| 1|ATX power supply. 250W is far enough.|
| 1|ATX PSU breakout module (see pictures).|
| 1|Power strip with 4 outlets.|
| 1|6A circuit breaker. I uded a Tomzin C6 model.|
| 1|Voltage and current meter (see pictures).|
| 4|Terminal bars (see pictures).|
| 1|Power plug.|
| 1|Power Switch. I used a margirius switch with protection cover.|
| 1|100K linear potentiometer (only if your breakout module came with a logarithmic one).|
| 1 meter|2.5mm blue wire, for internal wiring. Maybe you don´t need this, if you use the power strip cord.|
| 1 meter|2.5mm brown wire, for internal wiring. Maybe you don´t need this, if you use the power strip cord.|
| 1 ~ 2 meters|Main power cord with plug.|
| A lot|Nylon cable ties.|

## Notes

aaa

## Pictures

![PSU Module](images/panels/minilab-panel-psu.jpg)

