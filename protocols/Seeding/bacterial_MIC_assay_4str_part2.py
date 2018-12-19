# -*- coding: utf-8 -*-
'''

PART 2

This script has two different parts. On the first part, it distributes 
media from a single reservoir to the 6 different plates per columns, and an
aditional control plate which comes from the second reservoir. On the second 
part, it seeds those plates with the bacterial strains in the bacterial
reservoir.

Script by Dani Martinez, Nov - 2018
Cabreiro Lab. 
'''

from opentrons import labware, instruments, robot


#### load labware

# load 2 different plates
plate1 = labware.load('96-flat', '4') # loads a 96-flat plate
plate2 = labware.load('96-flat', '5') # loads a 96-flat plate

# bacteria
media = labware.load('trough-12row', '2') # loads a trough-12row
bacteria = labware.load('96-deep-well', '1') # loads a trough-12row

# tip racks
tiprack1 = labware.load('tiprack-200ul', '3') # loads a tip rack of 200 uL 

# pipette
pipette = instruments.P300_Multi(mount = 'right', tip_racks = [tiprack1])



#### actions

### first step: pour media in all plates 

## first half

# fill plate 1 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('1'), plate1.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 2 (half 1)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('2'), plate2.cols(i), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()


## second half

# fill plate 1 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('3'), plate1.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

# fill plate 2 (half 2)
pipette.pick_up_tip()
for i in range(6):
	pipette.transfer(150, media.cols('4'), plate2.cols(i + 6), 
		mix_before = (1, 100), new_tip = 'never')
pipette.drop_tip()

### second step: seed plates with bacteria

# loop that fills 

for i in range(12):
	pipette.pick_up_tip()
	# plate 1
	pipette.transfer(50, bacteria.cols(i), plate1.cols(i).top(), mix_befiore = (2, 100), new_tip = 'never')
	# plate 2
	pipette.transfer(50, bacteria.cols(i), plate2.cols(i).top(), mix_before = (2, 100), trash = True)


