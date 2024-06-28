const maxLevel = 20;
const maxAttribute = 18;
const races = ["Human", "Elf", "Dwarf"];
const races_base_HP = new Map([["Human", 20],["Elf",18],["Dwarf",22]]);
const classes = ["Fighter", "Spellsword", "Mage"];
const class_HP_per_lvl = new Map([["Fighter", 5],["Spellsword",4],["Mage",3]]);
export {maxLevel, maxAttribute, races, races_base_HP, classes, class_HP_per_lvl}

// Here we have a bunch of constant values to be exported to other scripts
// This way, we don't have a bunch of random "magic-numbers"
// Instead, they all refer back to this document, so they can easily be changed
