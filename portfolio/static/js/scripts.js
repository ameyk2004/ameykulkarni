function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to add typing animation to description when in viewport
function addTypingAnimation() {
    const description = document.getElementById('animatedDescription');
    if (isInViewport(description)) {
        description.querySelector('.card-text').classList.add('typing-animation');
    } else {
        description.querySelector('.card-text').classList.remove('typing-animation');
    }
}

// Event listener to check if description is in viewport on scroll
window.addEventListener('scroll', addTypingAnimation);

// Initial check on page load
addTypingAnimation();