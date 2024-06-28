/* wrote a script to automate writing out levels for the drop-down menu*/
/* since I was copying+pasting 20 times, and the lectures say you're probably doing something wrong at that point*/
/* this takes less overall code, and makes it simple to change the level-cap if I want! */

import {maxLevel} from "/constants.js";
var output = ``;

for (let i = 1; i <= maxLevel; i++)
{
    var line = `<option value="` + i + `">` + i + `</option>`;
    output += line;
}

var dropDownSelect = document.getElementById('levelSelect');
dropDownSelect.insertAdjacentHTML('beforeend', output);
