let lastIdea = "";
function addIdea() {
    let ideaText = document.getElementById("ideaInput")?.value;
    if (!ideaText) return;
    if (ideaText === "") {
        alert("Enter an idea, future visionary!");
        return;
    }
    let li = document.createElement("li");
    li.innerHTML = ideaText + '<span onclick="this.parentElement.remove()">X</span>';
    document.getElementById("ideaList").appendChild(li);
    lastIdea = ideaText;
    document.getElementById("ideaInput").value = "";
}

function inspireChange() {
    if (lastIdea === "") {
        alert("Add an idea first!");
        return;
    }
    const prefixes = ["Neo", "Hyper", "Quantum", "Astro", "Cyber"];
    const suffixes = ["Verse", "Sphere", "Nexus", "Shift", "Core"];
    let inspiredIdeas = [
        `${prefixes[Math.floor(Math.random() * prefixes.length)]}-${lastIdea}`,
        `${lastIdea} ${suffixes[Math.floor(Math.random() * suffixes.length)]}`,
        `${lastIdea} 2050`
    ];
    inspiredIdeas.forEach(idea => {
        let li = document.createElement("li");
        li.innerHTML = idea + '<span onclick="this.parentElement.remove()">X</span>';
        document.getElementById("ideaList").appendChild(li);
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const timelineItems = document.querySelectorAll(".timeline-item");
    if (timelineItems.length) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) entry.target.classList.add("visible");
            });
        }, { threshold: 0.3 });
        timelineItems.forEach(item => observer.observe(item));
    }
});
