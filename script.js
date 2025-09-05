function toggleMenu(){
    const m = document.querySelector(".menu-links");
    const i = document.querySelector(".fall-icon");
    m.classList.toggle("open");
    i.classList.toggle("open");
}

function scrollToNext() {
    const skillsSection = document.getElementById('skills');
    const offset = -110; // adjusted for proper scrolling to the skills section 
    const y = skillsSection.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top: y, behavior: 'smooth' });
  }



