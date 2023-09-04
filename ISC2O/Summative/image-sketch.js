/*Template for p5 Play library
Courtney Edwards - May 2021
This file shows an example for a sprite with an image*/

/* Benjamin Li, Aaron Yang - P-A2 Mini Game
Fruit Fetch - This game is based on "Catch the Fruit" */


// Define the variables
//This variable is to change the level
var level = 0;

//These two variables are the count of the apples and the bombs that have been collected
var apples = 0;
var bombs = 0;
var velocity = 0;

//This is to set up random generation of apples and bombs
var appleTimer = 250;
var bombTimer = 250;

//This is to check if the animation is happy or sad
var happyBool = false;
var sadBool = false;

//This is to hold timers for the happy and sad animations
var happyTimer = 0;
var sadTimer = 0;

//These are variables for images needed for the sprites
var forestImage;
var titleBg;
var basketImage;
var appleImage;
var bombImage
var heartImage

//These are the sprites in the game
var catSprite;
var basketSprite;
var appleSprite;
var bombSprite;
var heartSprite1;
var heartSprite2;
var heartSprite3;
var heartSprite4;
var heartSprite5;
var catSad;
var catHappy;
var catStand;

//These will be defined as groups that can hold the apple and bomb sprites
var appleGroup;
var bombGroup;

// preload function to preload the images
function preload(){
  //Preloading of all the images and their links

  //forest image source: https://www.artstation.com/artwork/g8oE9E
  forestImage = loadImage("forest.jpg");
  //title bg source: https://cutewallpaper.org/21/pixel-art-background-forest/view-page-21.html
  titleBg = loadImage("TitleBg.png")
  //cat image source: https://www.gameart2d.com/cat-and-dog-free-sprites.html
  catRun = loadAnimation("Run1.png", "Run8.png");
  catSad = loadAnimation("Hurt0.png", "Hurt9.png");
  catHappy = loadAnimation("Fall1.png", "Fall7.png");
  catStand = loadAnimation("Stand.png");
  //basket image source: http://pixelartmaker.com/art/d4a8495a2d5c3df
  basketImage = loadImage("basket.png");
  //apple image source: https://www.pngwing.com/en/free-png-nmmgd
  appleImage = loadImage("apple.png");
  //bomb image source: https://www.giantbomb.com/forums/general-discussion-30/gb-community-game-night-6725/
  bombImage = loadImage("bomb.png");
  //heart image source: https://opengameart.org/content/heart-pixel-art
  heartImage = loadImage("heart.png");

  // define appleGroup and bombGroup as groups
  appleGroup = new Group();
  bombGroup = new Group();
}

// setup function to add the sprites
function setup() {
  //Canvas
  createCanvas(775, 500);

  //This is to associate the basket and cat sprites with the images that were already preloaded, add necessary animations to the cat sprite, and give them their size and position

  //catsprite set up
  catSprite = createSprite(width/2, height/1.4);
  catSprite.addAnimation("Run", catRun);
  catSprite.addAnimation("Sad", catSad);
  catSprite.addAnimation("Happy", catHappy);
  catSprite.addAnimation("Stand", catStand);
  catSprite.scale = 0.3;

  //basketsprite set up
  basketSprite = createSprite(width/1.96, height/1.6);
  basketSprite.addImage(basketImage);
  basketSprite.scale = 0.38;

  // heart sprite setup to create all the heartsprites
    // It seems very repetitive but it was the only option that worked for us. 
    // We tried using groups and doing heartSprite2 = heartSprite1
    // but it did not work. We then tried using a function to get rid of repetitive
    // code, but it does not work because it is considered "outside of setup"
  // The x-position is off screen so the hearts only pop up when the level is 2
  // scale to decrease heart size

  heartSprite1 = createSprite(1000, 35);
  heartSprite1.addImage(heartImage);
  heartSprite1.scale = 0.2;

  heartSprite2 = createSprite(1000, 35);
  heartSprite2.addImage(heartImage);
  heartSprite2.scale = 0.2;
  
  heartSprite3 = createSprite(1000, 35);
  heartSprite3.addImage(heartImage);
  heartSprite3.scale = 0.2;
  
  heartSprite4 = createSprite(1000, 35);
  heartSprite4.addImage(heartImage);
  heartSprite4.scale = 0.2;
  
  heartSprite5 = createSprite(1000, 35);
  heartSprite5.addImage(heartImage);
  heartSprite5.scale = 0.2;
}

// draw function to implement everything and display it on the canvas
function draw() {
  //Level 0 title screen with sprites
  if (level == 0) {
    //make text colour blue
    fill(64, 224, 208);
    //change background to the titlebg forest
    background(titleBg);
    // change text size and write the title
    textSize(70);
    text('Fruit Fetch!', 225, 90);
    //make text colour red
    fill(253, 36, 65 );
    // change text size and write how to get to the instructions
    textSize(25);
    text('Press SPACE to view the instructions', 190, 455);
    //set the animation to stand so the cat will always be standing in the title screen
    catSprite.changeAnimation('Stand');
    
    //Sprites on screen with drawSprites function
    drawSprites();
  }

  //Level 1 instruction screen
  else if (level == 1) {
    //Text for instructions
    //change size and write How to Play
    textSize(48);
    text('How to Play!', 240, 80);
    // change size and write the instructions
    textSize(32);
    text('- Use keys A and D to move the character', 50, 150)
    text('around the forest!', 100, 200);
    text('- Collect 20 apples to win!', 50, 250);
    text('- Make sure to avoid bombs, if you collect', 50, 300);
    text('one, you lose a life!', 100, 350);
    text('Press SPACE to play!', 225, 450);
  }

  //Actual gameplay
  else if (level == 2) {
    //background set to forest
    background(forestImage);

    // this code sets the hearts on screen by changing the x-position
    // if no bombs are collected
    if(bombs == 0) {
      // draw 5 hearts on screen
      heartSprite1.position.x = 750;
      heartSprite2.position.x = 720;
      heartSprite3.position.x = 690;
      heartSprite4.position.x = 660;
      heartSprite5.position.x = 630;
    }
    // Move a heart off screen when 1 bomb is collected
    else if(bombs == 1) {
      heartSprite5.position.x = 1000;
    }
    // Move a heart off screen when 2 bombs are collected
    else if(bombs == 2) {
      heartSprite4.position.x = 1000;
    }
    // Move a heart off screen when 3 bombs are collected
    else if(bombs == 3) {
      heartSprite3.position.x = 1000;
    }
    // Move a heart off screen when 4 bombs are collected
    else if(bombs == 4) {
      heartSprite2.position.x = 1000;
    }
    // Move a heart off screen when 5 bombs are collected
    else if(bombs >= 5) {
      heartSprite1.position.x = 1000;
      // change to lose screen
      level = 4;
    }
    
    // function to move the cat and basket sprite. The function is defined below
    move(); 

    // This is to slow down the spawning of the apples using the appleTimer variable by making the appleTimer go up infinitely and spawning an apple when the appleTimer variable is 200. We also added a velocity command in order to make the apples fall down
    appleTimer++;
    if(appleTimer >= 200) {
      // add sprite at a random position
      appleSprite = createSprite(random(3, width-3), 0);
      appleSprite.addImage(appleImage);
      // make sprite smaller
      appleSprite.scale = 0.04;      
      // add sprite to appleGroup
      appleGroup.add(appleSprite);
      // change velocity
      appleSprite.velocity.y = 3;

      //This is to delete the apple once it goes off screen in order to allow the next apple to actually overlap with the cat
      if(appleGroup[0].position.y >= 400) {
        // remove the first element (apple) out of the appleGroup
        appleGroup.shift();
      }
      // reset the appleTimer. It does not start at 0 so the spawn times are not always the same
      appleTimer = random(0, 80);
    }

    //This is to slow down the spawning of the bombs using the bombTimer variable by making the bombTimer go up infinitely and spawning a bomb when the bombTimer variable is 200. We also added a velocity command in order to make the bombs fall down
    bombTimer++;
    if(bombTimer >= 400) {
      // add sprite at a random position
      bombSprite = createSprite(random(3, width-3), 0);
      bombSprite.addImage(bombImage);
      // make sprite smaller
      bombSprite.scale = 0.25;
      // add sprite to bombGroup
      bombGroup.add(bombSprite);
      // change velocity
      bombSprite.velocity.y = 3;

      //This is to delete the bomb once it goes off screen in order to allow the next bomb to actually overlap with the cat
      if(bombGroup[0].position.y >= 400) {
        // remove the first element (bomb) out of the bombGroup
        bombGroup.shift();
      }
      // reset the bombTimer. It does not start at 0 so the spawn times are not always the same
      bombTimer = random(0, 80);
    }
    // draw sprites to show the sprites on screen
    drawSprites();

    // This is to collect the apples and bombs when the sprites overlap. Refer to the collectApple and collectBomb functions below. 
    basketSprite.overlap(appleGroup, collectApple);
    basketSprite.overlap(bombGroup, collectBomb);

    //This is to change the cat's animation back to the running animation after a short amount of time. It checks for the variable happyTimer, and if that variable is above 30, it sets back to the running animation
    if(happyBool) {
      happyTimer++;
      if(happyTimer > 30) {
        // change the animation back to run
        catSprite.changeAnimation('Run');
        // reset the timer
        happyTimer = 0;
        // change the bool to false
        happyBool = false;
      }
    }
    //This is to change the cat's animation back to the running animation after a short amount of time. It checks for the variable sadTimer, and if that variable is above 30, it sets back to the running animation
    if(sadBool) {
      sadTimer++;
      if(sadTimer > 30) {
        // change the animation back to run
        catSprite.changeAnimation('Run');
        // reset the timer
        sadTimer = 0;
        // change the bool to false
        sadBool = false;
      }
    }

    //This is to set up the Fruit Collected and Bombs Collected count on the sides of the screen and adjust it to the amount of fruit and bombs collected
    // Make text white and change the text size
    fill(255, 255, 255);
    textSize(32);
    
    // Write the text for fruit collected
    text('Fruit Collected: ' + apples, 20, 50);
  }
  //Level 3 Win Screen
  else if (level == 3) {
    // move the hearts off screen as there will still be hearts remaining
    heartSprite1.position.x = 1000;
    heartSprite2.position.x = 1000;
    heartSprite3.position.x = 1000;
    heartSprite4.position.x = 1000;
    heartSprite5.position.x = 1000;

    // Black text
    fill(0, 0, 0);
    //Green Background
    background(144, 238, 144);
    //Win screen text and option to play again
    textSize(64);
    text('You Win!!!', 250, 100);
    textSize(32);
    text('Press SPACE to play again', 200, 400);
  }
  //Level 4 Lose Screen
  else if (level == 4) {
    // Black text
    fill(0, 0, 0);
    //Red Background
    background(185, 5, 5);
    //Lose screen text and option to play again
    textSize(64);
    text('You Lose...', 250, 100);
    textSize(32);
    text('Press SPACE to play again', 200, 400);
  }
}


// function to move the basket and cat
// also includes animation changes
function move() {
  // 1st in priority: change animation to happy/sad when cat collides with bomb/apple
  // if cat collides with bomb
  if(basketSprite.overlap(appleGroup, collectApple)) {
    //changing the animation every the cat collects an apple
    catSprite.changeAnimation('Happy');
    // this is to help change the cat animation to "happy"
    happyBool = true;
    
  // else if cat collides with apple
  } else if(basketSprite.overlap(bombGroup, collectBomb)) {
    //change the animation every time the cat collects a bomb
    catSprite.changeAnimation('Sad');
    // this is to help change the cat animation to "sad"
    sadBool = true;

  // 2nd in priority: change animation to running when A or D is pressed
  } else if(keyIsDown(65)) {
    // if the cat is currently not in the happy or sad animation
    // change the animation to run
    if(!happyBool && !sadBool) {
      catSprite.changeAnimation('Run');
    }
    // if "a" is pressed, face left and decrease x-velocity by 5
    catSprite.mirrorX(-1);
    velocity = -5;
    
  } else if(keyIsDown(68)) {
    // if the cat is currently not in the happy or sad animation
    // change the animation to run
    if(!happyBool && !sadBool) {
      catSprite.changeAnimation('Run');
    }
    // if "d" is pressed, face right and increase x-velocity by 5
    catSprite.mirrorX(1);
    velocity = 5;  

  // last in priority: change animation to stand when nothing is pressed
  } else {
    // if the cat is currently not in the happy or sad animation
    // change the animation to stand
    if(!happyBool && !sadBool) {
      catSprite.changeAnimation('Stand');
    }
    // if neither A or D are pressed, make x-velocity 0
    velocity = 0;
  }

  //function to set the velocity variable to the cat and the basket's actual x velocity
  catSprite.velocity.x = velocity;
  basketSprite.velocity.x = velocity;

  //function to not allow the cat to leave the screen using conditional statements
  if(catSprite.position.x > width-10) {
    // if the cat is outside the screen on the right side, push it back
    catSprite.position.x = width-10;
    // the basket too
    basketSprite.position.x = width-5;
  }
  else if(catSprite.position.x < 10) {
    // if the cat is outside the screen on the left side, push it back
    catSprite.position.x = 10;
    // the basket too
    basketSprite.position.x = 20;
  }
}


// function to get rid of apple when in contact with cat
// first parameter - the basket
// second parameter - the apple
function collectApple(basket, apple) {
  //remove the apple sprite when collision happens
  apple.remove();
  // this is to keep track of the number of apples collected
  apples++;
  
  
  //Change to win screen when 20 apples are collected
  if(apples >= 20) {
    level = 3;
  }
}


// function to get rid of bomb when in contact with cat
// first parameter - the basket
// second parameter - the bomb
function collectBomb(basket, bomb) {
  // remove the bomb sprite when collision happens
  bomb.remove();
  // this is to keep track of the number of bombs collected
  bombs++;
}


// keypressed function to change levels whenever SPACE is pressed, and limits being set to not allow exploits. e.g: you cannot press space to change levels after level 1, and if level is greater than 4, it resets back to 0
function keyPressed() {
  // if the level is 3 or 4 (win/lose screen)
  if(keyCode == 32 && (level == 3 || level == 4)) {
    // clear then set level and apple/bomb-count to 0
    clear();
    level = 0;
    apples = 0;
    bombs = 0;

    // If the user holds A or D as they were about to win/lose, then the cat would move off screen. This is to make sure this doesnt happen
    catSprite.velocity.x = 0;
    basketSprite.velocity.x = 0;
    // set catSprite and basketSprite position to the centre of the screen
    catSprite.position.x = width/2;
    basketSprite.position.x = width/1.96;
    // make the cat face right
    catSprite.mirrorX(1);

    // There was a bug that showed falling apples/bombs in level 0 so we got them out of the screen by increasing the velocity to a speed where it is so fast that is it not even on the screen.
    bombSprite.velocity.y = 10000;
    appleSprite.velocity.y = 10000;
  }
  // else if the level is 0 or 1 (Title/introduction screen)
  else if (keyCode == 32 && (level == 0 || level == 1)) {
    // clear then increase level by 1
    clear();
    level++;
  }
}