function toggleMenu(){
    const m = document.querySelector(".menu-links");
    const i = document.querySelector(".fall-icon");
    m.classList.toggle("open");
    i.classList.toggle("open");
}

function scrollToSkills() {
    const skillsSection = document.getElementById('skills');
    const offset = -110; // adjusted for proper scrolling to the skills section 
    const y = skillsSection.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top: y, behavior: 'smooth' });
  }

  function scrollToAbout() {
    const aboutSection = document.getElementById('about');
    const offset = -100; // adjusted for proper scrolling to the about section 
    const y = aboutSection.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top: y, behavior: 'smooth' });
  }

// Snake Game
const canvas = document.getElementById('snakeGame');
const ctx = canvas.getContext('2d');
const scoreElement = document.getElementById('score');

// Game state
let snake = [];
let food = { x: 0, y: 0 };
let dx = 0;
let dy = 0;
let score = 0;
let gameInterval;
let isGameRunning = false;

// Constants
const GRID_SIZE = 20;
const TILE_COUNT = canvas.width / GRID_SIZE;
const GAME_SPEED = 100;

// Skill Images for Food
const skillImagesSources = [
    './Images/pythonlogo.png',
    './Images/sqllogo.png',
    './Images/Clogo.png',
    './Images/csharplogo.png',
    './Images/Java-Logo.png',
    './Images/jslogo.png',
    './Images/htmllogo.png',
    './Images/csslogo.png',
    './Images/typescript_logo.png',
    './Images/React_Logo.png',
    './Images/flask_logo.png',
    './Images/git_logo.png'
];

let loadedImages = [];
let currentFoodImage = null;

// Preload images
skillImagesSources.forEach(src => {
    const img = new Image();
    img.src = src;
    loadedImages.push(img);
});

function generateFood() {
    food = {
        x: Math.floor(Math.random() * TILE_COUNT),
        y: Math.floor(Math.random() * TILE_COUNT)
    };
    // Check if food spawns on snake
    for (let segment of snake) {
        if (segment.x === food.x && segment.y === food.y) {
            generateFood();
            break;
        }
    }
    // Randomly select a skill image for this food
    if (loadedImages.length > 0) {
        currentFoodImage = loadedImages[Math.floor(Math.random() * loadedImages.length)];
    }
}

function resetGame() {
    if (!canvas) return;
    clearInterval(gameInterval);
    snake = [{ x: 10, y: 10 }];
    dx = 0;
    dy = 0;
    score = 0;
    if(scoreElement) scoreElement.textContent = score;
    isGameRunning = false;
    currentFoodImage = null; // Clear image initially until start/reset calls generateFood
    generateFood();
    draw();
}

function startGame() {
    if (isGameRunning) return;
    resetGame();
    isGameRunning = true;
    dx = 1; // Start moving right
    dy = 0;
    gameInterval = setInterval(gameLoop, GAME_SPEED);
}

function gameLoop() {
    update();
    draw();
}

function update() {
    // Move snake
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };

    // Check collision with walls
    if (head.x < 0 || head.x >= TILE_COUNT || head.y < 0 || head.y >= TILE_COUNT) {
        gameOver();
        return;
    }

    // Check collision with self
    for (let i = 0; i < snake.length; i++) {
        if (head.x === snake[i].x && head.y === snake[i].y) {
            gameOver();
            return;
        }
    }

    snake.unshift(head);

    // Check food collision
    if (head.x === food.x && head.y === food.y) {
        score += 10;
        scoreElement.textContent = score;
        generateFood();
    } else {
        snake.pop();
    }
}

function draw() {
    if (!ctx) return;
    // Clear canvas
    ctx.fillStyle = '#5da34ae0';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw snake
    ctx.fillStyle = '#4CAF50';
    snake.forEach((segment, index) => {
        // Head is slightly different color
        if (index === 0) ctx.fillStyle = '#5134d4ff';
        else ctx.fillStyle = '#624dc0ff';
        
        ctx.fillRect(segment.x * GRID_SIZE, segment.y * GRID_SIZE, GRID_SIZE - 2, GRID_SIZE - 2);
    });

    // Draw food
    if (currentFoodImage && currentFoodImage.complete) {
        // Draw the image if loaded
        // Make food slightly larger (1.5x grid size) and center it
        const scale = 1.5;
        const size = GRID_SIZE * scale;
        const offset = (size - GRID_SIZE) / 2;
        
         ctx.drawImage(
            currentFoodImage,
            food.x * GRID_SIZE - offset,
            food.y * GRID_SIZE - offset,
            size,
            size
        );
    } else {
        // Fallback to red dot if image isn't ready
        ctx.fillStyle = '#FF5252';
        ctx.beginPath();
        ctx.arc(
            food.x * GRID_SIZE + GRID_SIZE/2, 
            food.y * GRID_SIZE + GRID_SIZE/2, 
            GRID_SIZE/2 - 2, 
            0, 
            Math.PI * 2
        );
        ctx.fill();
    }
}

// Modal Logic
const modal = document.getElementById("game-modal");
const closeModalSpan = document.getElementsByClassName("close-modal")[0];
const finalScoreSpan = document.getElementById("final-score");

function gameOver() {
    clearInterval(gameInterval);
    isGameRunning = false;
    // alert(`Game Over! Score: ${score}`);
    if (finalScoreSpan) finalScoreSpan.textContent = score;
    if (modal) modal.style.display = "block";
}

function restartGameFromModal() {
    if (modal) modal.style.display = "none";
    startGame();
}

function closeModal() {
    if (modal) modal.style.display = "none";
    resetGame();
}

// Close modal if user clicks outside of it
window.onclick = function(event) {
    if (event.target == modal) {
        closeModal();
    }
}

function handleInput(e) {
    if (["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight"].includes(e.key)) {
        e.preventDefault(); // Prevent scrolling
    }

    if (!isGameRunning) return;

    switch(e.key) {
        case 'ArrowUp':
            if (dy !== 1) { dx = 0; dy = -1; }
            break;
        case 'ArrowDown':
            if (dy !== -1) { dx = 0; dy = 1; }
            break;
        case 'ArrowLeft':
            if (dx !== 1) { dx = -1; dy = 0; }
            break;
        case 'ArrowRight':
            if (dx !== -1) { dx = 1; dy = 0; }
            break;
    }
}

// Event Listeners
document.addEventListener('keydown', handleInput);

// Initial draw logic 
// Wait for DOM content to be loaded if script is in head, but it is at end of body so it's fine.
if (canvas) {
    resetGame();
}

// Project Section Animations
function initProjectAnimations() {
    const cards = document.querySelectorAll('.details-container-projects');
    
    if (cards.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('animate-in');
                }, index * 100);
                observer.unobserve(entry.target);
            }
        });
    }, { 
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    cards.forEach(card => observer.observe(card));
}

// Initialize project animations when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initProjectAnimations);
} else {
    initProjectAnimations();
}



