import {classes} from "/constants.js";
import {class_HP_per_lvl} from "/constants.js";

var output = ``;
var hp_per_lvl = 0;
var PC_class = '';

for (let index = 0, indexLength = classes.length; index < indexLength; index++)
{
    PC_class = classes[index];
    hp_per_lvl = class_HP_per_lvl.get(PC_class);
    output += `<option value="` + hp_per_lvl + `">` + PC_class + `</option>`;
}

document.getElementById('classSelect').innerHTML = output;
