/*
Another auto-generated list, although this one could've been done manually
Will save a little bit of effort if more races are added,
although I'd still need to make the new html-page for it.
*/
import {races} from "/constants.js";
import {races_base_HP} from "/constants.js";

var output = ``;
var base_hp = 0;
var race = '';
for (let index = 0, indexLength = races.length; index < indexLength; index++)
{

    //line = index + 1;
    race = races[index];
    base_hp = races_base_HP.get(race);
    //console.log(base_hp);
    output += `<option value="` + base_hp + `">` + race + `</option>`;
}

document.getElementById('raceSelect').innerHTML = output;
