setTimeout(function() {
            const messages = document.querySelectorAll('.messages .alert');
            messages.forEach(function(message) {
                message.style.display = 'none';
            });
        }, 3000);

const titles = ["Web Developer", "Automation Developer", "Software Developer"];
    let currentIndex = 0;
    const titleElement = document.getElementById("developer-title");

    function changeTitle() {
        titleElement.classList.remove("typing"); // Remove typing animation class
        titleElement.textContent = titles[currentIndex];
        currentIndex = (currentIndex + 1) % titles.length;
        setTimeout(() => titleElement.classList.add("typing"), 100); // Add typing class after content changes
    }

    setInterval(changeTitle, 4000);  // Change title every 4 seconds
    changeTitle();  // Initially set the first title

    console.log(200)