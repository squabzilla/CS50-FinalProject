var nav =
`<nav class="nav bg-primary" >` +
`    <a class="nav-link link-dark" href="index.html"><b><u>Home</u></b></a>` +
`    <a class="nav-link link-dark"><b>Races:</b></a>` +
`    <a class="nav-link link-dark" href="human.html"><u>Human</u></a>` +
`    <a class="nav-link link-dark" href="elf.html"><u>Elf</u></a>` +
`    <a class="nav-link link-dark" href="dwarf.html"><u>Dwarf</u></a>` +
`    <a class="nav-link link-dark"><b>Classes:</b></a>` +
`    <a class="nav-link link-dark" href="fighter.html"><u>Fighter</u></a>` +
`    <a class="nav-link link-dark" href="spellsword.html"><u>Spellsword</u></a>` +
`    <a class="nav-link link-dark" href="mage.html"><u>Mage</u></a>` +
`    <a class="nav-link link-dark" href="character.html"><b><u>Create A Character</u></b></a>` +
`    <a class="nav-link link-dark">|</a>` +
`    <a class="nav-link link-dark" id="Current_Page"></a>` +
`</nav>`;

var nav_pane = document.getElementById('nav_pane'); // target element.
nav_pane.insertAdjacentHTML('beforeend', nav); // add content.

var page_title = document.getElementById('Page_Title').innerHTML;
document.getElementById('Current_Page').innerHTML = "<i>Current page: </i><b>" + page_title +"</b>";

/*
With the help of bootstrap, I have
*/
