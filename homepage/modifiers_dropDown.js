/*
Since I had a script for the levels drop-down, I decided to add one for the attributes-down-down as well.
While the list of attributes isn't entirely dynamic, the character creation page will need to be
updated manually anyways for different scripts that calculate values based on this.
I DID actually try auto-generating scripts for different attributes
But then I ran into a bunch of scope-errors, and figured I should abort
Dunno how accessible my files are outside of ones specifically submitted,
but I have a homepage_old directory full of that failed attempt.
*/

/*
Note that we loop through all the attributes, insead of copying it for each attribute
*/

import {maxAttribute} from "/constants.js";
var attributesSelectList = ["str_select", "dex_select", "con_select", "int_select", "wis_select", "cha_select"];
var output = ``;
var dropDownSelect;
for (let index = 0, len = attributesSelectList.length; index < len; index++)
{
    // a nested loop for the selectable-values of the drop-down menus
    for (let i = 1; i <= maxAttribute; i++)
    {
        output += `<option value="` + i + `">` + i + `</option> `;
    }
    dropDownSelect = document.getElementById(attributesSelectList[index]);
    dropDownSelect.insertAdjacentHTML('beforeend', output);
    var output = ``;
}
