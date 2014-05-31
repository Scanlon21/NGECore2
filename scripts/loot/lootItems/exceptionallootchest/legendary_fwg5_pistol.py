
def itemTemplate():

	return ['object/weapon/ranged/pistol/shared_pistol_fwg5_legendary.iff']

def customItemName():

	return 'Legendary FWG5 Pistol'
	
def customItemStackCount():

	return 1
	
def customizationAttributes():

	return []
	
def customizationValues():

	return []
	
def requiredCL():

	return 88

def itemStats():

	stats = ['mindamage','250','270']
	stats += ['maxdamage','500','530']
	stats += ['attackspeed','0.4','0.4']
	stats += ['maxrange','0','35']
	stats += ['damagetype','energy','energy']
	stats += ['elemtype','@obj_attr_n:elemental_heat','@obj_attr_n:elemental_heat']
	stats += ['elemdamage','35','35']
	stats += ['weapontype','2','2']
	
	return stats 
