if (myChoice == "drag1"){
    myGameArea.main_character == "pacman";
    pacman_img.src = 'images/pacman.png';
    blue_ghost_img.src = 'images/blue-ghost.png';
    orange_ghost_img.src = 'images/orange-ghost.png';
    red_ghost_img.src = 'images/red-ghost.png';
    white_dot_img.src = 'images/whitedot.png';
    myBackgroundMusic = new sound("sounds/dp-atw.mp3");
} else if (myChoice == "drag2") {
    myGameArea.main_character == "pikachu";
    pacman_img.src = 'images/pika-pacman.png';
    blue_ghost_img.src = 'images/gengar.png';
    orange_ghost_img.src = 'images/poke-skull.png';
    red_ghost_img.src = 'images/haunter.png';
    white_dot_img.src = 'images/pokeball.png';
    myBackgroundMusic = new sound("sounds/pokemon.ogg");
} else if (myChoice == "drag3") {
  myGameArea.main_character == "link";
  pacman_img.src = 'images/link.png';
  blue_ghost_img.src = 'images/skull.png';
  orange_ghost_img.src = 'images/skull.png';
  red_ghost_img.src = 'images/skull.png';
  white_dot_img.src = 'images/rupee.png';
  myBackgroundMusic = new sound("sounds/zelda.ogg");
} else {
  alert("Selecciona personaje!");
  location.reload();
  //myPacman = new component(40, 40, 330, 330, 0, 0, pacman_img,'char');
}


<div id="charsel">
<center>
<div id="draganddrop" ondrop="drop(event)" ondragover="allowDrop(event)"></div>
<br>
<div style="background-color:black;width:600px;">
<img id="drag1" src="images/pacman.png" draggable="true" ondragstart="drag(event)" width="150" height="150">
<img id="drag2" src="images/pika-pacman.png" draggable="true" ondragstart="drag(event)" width="150" height="150">
<img id="drag3" src="images/link.png" draggable="true" ondragstart="drag(event)" width="150" height="150">
</div>



myScoreText.text="SCORE: " + String(myScore);
myLivesText.text="Lives: " + String(myLives);

for (i = 0; i < myTexts.length; i += 1) {
  myTexts[i].update();
}




var myChar1_img = new DragImage('images/pacman.png', 60, 60);
var myChar2_img = new DragImage('images/pika-pacman.png', 60, 60);
var myChar3_img = new DragImage('images/link.png', 60, 60);
