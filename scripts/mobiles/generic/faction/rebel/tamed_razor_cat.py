import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('rebel_tamed_razor_cat')
	mobileTemplate.setLevel(10)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Carnivore Meat")
	mobileTemplate.setMeatAmount(65)
	mobileTemplate.setHideType("Bristly Hide")
	mobileTemplate.setHideAmount(35)
	mobileTemplate.setBoneType("Mammal Bones")
	mobileTemplate.setBoneAmount(30)
	mobileTemplate.setSocialGroup("razor cat")
	mobileTemplate.setAssistRange(0)
	mobileTemplate.setStalker(True)
	mobileTemplate.setFaction("rebel")
	mobileTemplate.setFactionStatus(1)
	
	templates = Vector()
	templates.add('object/mobile/shared_corellian_sand_panther.iff')
	mobileTemplate.setTemplates(templates)
	
	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)
	
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('tamed_razor_cat', mobileTemplate)
	return