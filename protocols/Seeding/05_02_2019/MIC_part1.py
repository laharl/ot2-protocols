# -*- coding: utf-8 -*-
'''
MIC experiment, two parts. 

The first part will add all the media1 to each plate. Each plate will have 4 columns
with a different drug concentration starting from 0, to 1024 uM of 5FU.

Script by Dani Martinez, May - 2019
'''

from opentrons import labware, instruments, robot


#### load labware

# load 4 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '7') # loads a 96-flat plate
plate3 = labware.load('96-flat', '8') # loads a 96-flat plate
plate4 = labware.load('96-flat', '10') # loads a 96-flat plate
plate5 = labware.load('96-flat', '11') # loads a 96-flat plate


# reservoir
media1 = labware.load('trough-12row', '1') # loads a 12 column reservoir
media2 = labware.load('trough-12row', '2') # loads a 12 column reservoir

# tiprack
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 
tiprack2 = labware.load('tiprack-200ul', '6') # loads a tip rack of 200 uL 


# pipette
pipette = instruments.P300_Multi(mount = 'left', tip_racks = [tiprack1, tiprack2])


## Plate 1
pipette.pick_up_tip()
for i in [0,1,2,3]:
	pipette.transfer(150, media1.cols('1'), plate1.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [4,5,6,7]:
	pipette.transfer(150, media1.cols('2'), plate1.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [8,9,10,11]:
	pipette.transfer(150, media1.cols('3'), plate1.cols(i), new_tip = 'never')
pipette.drop_tip()



## Plate 2
pipette.pick_up_tip()
for i in [0,1,2,3]:
	pipette.transfer(150, media1.cols('4'), plate2.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [4,5,6,7]:
	pipette.transfer(150, media1.cols('5'), plate2.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [8,9,10,11]:
	pipette.transfer(150, media1.cols('6'), plate2.cols(i), new_tip = 'never')
pipette.drop_tip()


## Plate 3
pipette.pick_up_tip()
for i in [0,1,2,3]:
	pipette.transfer(150, media1.cols('7'), plate3.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [4,5,6,7]:
	pipette.transfer(150, media1.cols('8'), plate3.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [8,9,10,11]:
	pipette.transfer(150, media1.cols('9'), plate3.cols(i), new_tip = 'never')
pipette.drop_tip()


## Plate 4
pipette.pick_up_tip()
for i in [0,1,2,3]:
	pipette.transfer(150, media1.cols('10'), plate4.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [4,5,6,7]:
	pipette.transfer(150, media1.cols('11'), plate4.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [8,9,10,11]:
	pipette.transfer(150, media1.cols('12'), plate4.cols(i), new_tip = 'never')
pipette.drop_tip()


## Plate 5
pipette.pick_up_tip()
for i in [0,1,2,3]:
	pipette.transfer(150, media2.cols('1'), plate5.cols(i), new_tip = 'never')
pipette.drop_tip()

pipette.pick_up_tip()
for i in [4,5,6,7]:
	pipette.transfer(150, media2.cols('2'), plate5.cols(i), new_tip = 'never')
pipette.drop_tip()
