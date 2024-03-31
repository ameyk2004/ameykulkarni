
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate__animated', 'animate__fadeIn');
        } else {
            entry.target.classList.remove('animate__animated', 'animate__fadeIn');
        }
    });
});

const elements = document.querySelectorAll('.col'); // Select elements to animate

elements.forEach(element => {
    observer.observe(element);
});
onst hinjewadiCard = document.getElementById('hinjewadi-card');

// Function to check if the element is in the viewport
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight)
  );
}

// Function to handle scroll event
function handleScroll() {
  if (isInViewport(hinjewadiCard)) {
    // Add the animation class when the element is in the viewport
    hinjewadiCard.classList.add('animate__fadeInLeft');
  }
}

// Add scroll event listener to the window
window.addEventListener('scroll', handleScroll);

// Initial check when the page loads
handleScroll();
AOS.init();
document.addEventListener("DOMContentLoaded", function() {
    const typingText = document.querySelector(".typing-text");
    const text = typingText.innerText;
    typingText.innerText = ""; // Clear the original text

    for (let i = 0; i < text.length; i++) {
        const char = text.charAt(i);
        const span = document.createElement("span");
        span.innerText = char;
        span.style.animationDelay = `${i * 0.1}s`; // Adjust the delay based on the typing speed
        typingText.appendChild(span);
    }
});
