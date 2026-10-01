"""Skills from the current resume, plus tools already documented in the portfolio."""
SKILLS = {
    'Languages': [
        ('TypeScript', 'Typed application code for microservices, developer tooling, and web interfaces.'),
        ('Python', 'Backend services and scripting, including the Flask playlist generator.'),
        ('JavaScript', 'Browser interactions and server-side application logic.'),
        ('Java', 'Object-oriented programming and software engineering fundamentals.'),
        ('C++', 'Systems programming with explicit control over memory and data structures.'),
        ('C#', 'Unity gameplay code, including enemy behavior and level progression.'),
        ('SQL', 'Querying and working with relational application data.'),
        ('C', 'Low-level programming fundamentals and memory management.'),
    ],
    'Frontend': [
        ('React.js', 'Interfaces for TEDxThirdWard, NutriScan, and browser-based experiments.'),
        ('Vue.js', 'Component-based web interfaces and reactive application state.'),
        ('HTML', 'Semantic page structure that works before JavaScript loads.'),
        ('CSS', 'Responsive layouts, motion, and visual styling.'),
        ('Tailwind CSS', 'Utility-based styling for React applications.'),
        ('Redux Toolkit', 'Shared application state in Open Cam Lab.'),
    ],
    'Backend & data': [
        ('Node.js', 'Production TypeScript services, serverless functions, and agent tooling.'),
        ('FastAPI', 'Python APIs with typed request and response models.'),
        ('Flask', 'The Python backend connecting the playlist generator to Spotify.'),
        ('PostgreSQL', 'Relational storage for TEDxThirdWard and RoleColorFinder.'),
        ('Redis', 'In-memory data storage for caching and fast lookups.'),
        ('Supabase', 'PostgreSQL-backed production services and authentication for RoleColorFinder.'),
        ('MySQL', 'Relational databases and SQL-based application data.'),
        ('REST APIs', 'HTTP interfaces between frontends, services, and external integrations.'),
        ('Stripe', 'Customer billing and payment integration for RoleColorFinder.'),
    ],
    'Cloud': [
        ('AWS', 'Production infrastructure and automation across multiple AWS accounts.'),
        ('RDS', 'Managed relational databases on AWS.'),
        ('S3', 'Object storage for files and application assets.'),
        ('SQS', 'Queues for asynchronous work between services.'),
        ('SNS', 'Publish-subscribe messaging and notifications.'),
        ('EKS', 'Managed Kubernetes, including a sandbox promotion to pre-production.'),
        ('Kubernetes', 'Deployments and operational workflows spanning nine clusters.'),
        ('Docker', 'Containerized applications and consistent runtime environments.'),
        ('Vercel', 'Web application and serverless deployments.'),
        ('AWS Amplify', 'Hosting and deployment for Open Cam Lab.'),
    ],
    'Delivery': [
        ('Git / GitHub', 'Version control, shared repositories, and code reviews.'),
        ('CI/CD', 'Automated validation and production releases across four environments.'),
        ('Azure DevOps', 'Build and release pipelines for production services.'),
        ('ArgoCD', 'GitOps-based deployment of Kubernetes applications.'),
        ('Temporal', 'Workers and durable workflows across shared platform services.'),
        ('Playwright', 'Browser tooling for Arden and automated browser workflows.'),
        ('RIO', 'Part of the production engineering stack in my ConvergentIS role.'),
        ('SAP IAS', 'Identity services within the enterprise platform stack.'),
        ('Unity', 'A low-poly RPG with puzzles, enemy AI, and a final boss.'),
    ],
    'AI & tooling': [
        ('Claude Code', 'AI-assisted developer workflows and reviewed cloud security automation.'),
        ('MCP', 'Connecting AI-assisted workflows to tools and cloud operations.'),
        ('TensorFlow.js', 'Machine learning models running in JavaScript.'),
        ('Gemini', 'Multimodal photo input and meal-planning output in NutriScan.'),
        ('DigitalOcean', 'NutriScan deployment and Gradient AI integration.'),
        ('face-api.js', 'Real-time browser face detection in Open Cam Lab.'),
        ('Claude / OpenAI', 'Model integrations in Arden’s model-agnostic agent architecture.'),
        ('Bland AI', 'Voice automation in the Arden project stack.'),
    ],
}

# Personal examples come from the resume and existing project write-ups.
STORIES = {
    'TypeScript': 'I use TypeScript across 10+ services and Temporal workers at ConvergentIS. It also connects my work on RoleColorFinder with my own agent project, Arden.',
    'Python': 'I built the playlist generator with Python and Flask. That project taught me to plan the request flow before connecting an interface to a third-party API.',
    'JavaScript': 'My first portfolio was handmade with HTML, CSS, and JavaScript. This site still uses that foundation, including the wheel you just spun.',
    'HTML': 'My first portfolio started here: writing the page structure myself. The original is still archived in this repository, and the current site keeps its content in static HTML.',
    'CSS': 'I used CSS to style my first handmade portfolio. In this version, it handles the responsive layouts and keeps every label upright as this wheel turns.',
    'C#': 'I worked with a team of four on Escape PolyLand in Unity. Building its enemy behavior, puzzles, and progression taught me to split large features into smaller systems.',
    'React.js': 'I used React for the public TEDxThirdWard site and its admin console. The interesting part was making content updates usable for people who do not write code.',
    'Node.js': 'At ConvergentIS, I build fixes across TypeScript and Node.js microservices. I also used Node.js for Arden’s model-agnostic agent architecture.',
    'Flask': 'I built a Flask backend around Spotify’s API for my playlist generator. Clear endpoints helped me keep the music-selection flow manageable.',
    'PostgreSQL': 'I worked with PostgreSQL for TEDxThirdWard’s content and RoleColorFinder’s production services. Both connect user-facing interfaces to relational data.',
    'Supabase': 'At RoleColorFinder, I use Supabase and PostgreSQL for production services, including authentication. That work sits alongside billing and the customer-facing product.',
    'Stripe': 'I integrated billing into RoleColorFinder’s production services. It is part of the work that moved the platform into early revenue.',
    'AWS': 'My ConvergentIS work includes production infrastructure and reviewed security automation across multiple AWS accounts. As an intern, I also helped promote an EKS sandbox into pre-production.',
    'EKS': 'During my internship, I led the promotion of a sandbox EKS environment to pre-production. The work included validating release workflows across more than ten microservices.',
    'Kubernetes': 'I build repeatable workflows spanning nine Kubernetes clusters at ConvergentIS. Making specialized operational tasks usable by other engineers is a big part of that work.',
    'Docker': 'Docker is part of my Junior Software Engineer stack at ConvergentIS, alongside Kubernetes, TypeScript services, and Temporal workers.',
    'Vercel': 'I deployed TEDxThirdWard on Vercel and use it in RoleColorFinder’s production stack. Those projects combine web interfaces with backend services.',
    'AWS Amplify': 'I deployed Open Cam Lab on AWS Amplify to take a browser-based computer vision experiment through a cloud deployment.',
    'Git / GitHub': 'Collaborating on Escape PolyLand made version control essential. At RoleColorFinder, code reviews and frequent releases are also part of how I lead engineering work.',
    'CI/CD': 'I own production releases across four environments at ConvergentIS. That means coordinating readiness and carrying changes through deployment, not just getting a build to pass.',
    'Azure DevOps': 'I work with Azure DevOps in the production release stack at ConvergentIS. My responsibilities include CI/CD, cross-environment changes, and deployment readiness.',
    'ArgoCD': 'ArgoCD is part of the GitOps workflow I use for Kubernetes deployments at ConvergentIS, where I own releases across four environments.',
    'Temporal': 'I work on Temporal workers at ConvergentIS. One reliability issue involved recurring worker outages traced to database credential rotation and a more resilient recovery path.',
    'Playwright': 'I built Playwright browser tooling into Arden so the agent could interact with the browser as part of autonomous task execution.',
    'Unity': 'Escape PolyLand was a team project with enemy AI, puzzles, multiple levels, and a final boss. It taught me how much game development depends on clear ownership and smaller testable systems.',
    'Claude Code': 'During my internship, I built Claude Code and MCP automation to audit cloud security across AWS accounts. I reviewed and validated the changes as part of improving SOC 2 preparedness.',
    'MCP': 'I paired MCP with Claude Code for cloud security automation at ConvergentIS. The workflow connected tools to the audit and remediation process, with changes reviewed before use.',
    'Gemini': 'At HackWestern 12, our team used Gemini’s vision capabilities in NutriScan. We had 36 hours to connect photo input, model output, and meal suggestions into a working demo.',
    'DigitalOcean': 'Our NutriScan team deployed on DigitalOcean and used Gradient AI. The project won Best Use of DigitalOcean AI alongside Sun Life Best Health Hack.',
    'face-api.js': 'I used face-api.js in Open Cam Lab for live face detection and image uploads. The challenge was keeping the interface responsive while processing camera frames.',
    'Redux Toolkit': 'I used Redux Toolkit in Open Cam Lab to manage application state around live detection, image uploads, and the interface.',
    'Tailwind CSS': 'I used Tailwind in TEDxThirdWard and NutriScan. On the hackathon project, it helped the team put a working interface together within the 36-hour sprint.',
    'Claude / OpenAI': 'I designed Arden to support Claude, OpenAI, and other models. The TypeScript architecture connects model calls to tools, memory, and autonomous tasks.',
    'Bland AI': 'Bland AI is part of Arden’s voice automation stack, alongside model integrations, browser tooling, and messaging.',
}

def story_for(name, category, description):
    return experience_for(name, description)

PRODUCTION = {'TypeScript', 'Node.js', 'PostgreSQL', 'Supabase', 'Stripe', 'AWS', 'EKS', 'Kubernetes', 'Docker', 'Vercel', 'Git / GitHub', 'CI/CD', 'Azure DevOps', 'ArgoCD', 'Temporal', 'Claude Code', 'MCP', 'RIO', 'SAP IAS', 'React.js', 'Tailwind CSS'}
PROJECT_USE = {'Python', 'JavaScript', 'HTML', 'CSS', 'C#', 'Flask', 'AWS Amplify', 'Playwright', 'Unity', 'Gemini', 'DigitalOcean', 'face-api.js', 'Redux Toolkit', 'Claude / OpenAI', 'Bland AI'}

def experience_for(name, description):
    if name in PRODUCTION:
        return 'Production experience. ' + STORIES.get(name, description)
    if name in PROJECT_USE:
        return 'Project experience. ' + STORIES.get(name, description)
    if name in {'RDS', 'S3', 'SQS', 'SNS'}:
        return 'Part of my AWS toolkit. ' + description
    return 'In my technical toolkit. ' + description

def render_skills():
    from html import escape
    categories = ''.join(f'<button type="button" data-skill-category="{escape(category)}" aria-pressed="{str(i == 0).lower()}">{escape(category)}</button>' for i,category in enumerate(SKILLS))
    groups = ''.join('<section class="skill-directory-group"><h2>'+escape(category)+'</h2><div class="skill-directory-grid">'+''.join(f'<article data-skill="{escape(name, quote=True)}" data-skill-group="{escape(category, quote=True)}" data-summary="{escape(description, quote=True)}" data-story="{escape(story_for(name, category, description), quote=True)}"><h3>{escape(name)}</h3><p>{escape(experience_for(name, description))}</p></article>' for name,description in items)+'</div></section>' for category,items in SKILLS.items())
    return '''<section class="skills-explorer" aria-label="Interactive skills wheel"><div class="skill-categories" role="group" aria-label="Choose a skill category">'''+categories+'''</div><div class="wheel-layout"><div class="skill-wheel" tabindex="0" role="group" aria-label="Spin the skills wheel" aria-describedby="wheel-help"><span class="wheel-pointer" aria-hidden="true">▼</span><div class="wheel-ring"></div><div class="wheel-ring inner"></div><div class="wheel-rotor" id="wheel-rotor"></div><div class="wheel-center" aria-live="polite" aria-atomic="true"><span id="wheel-category">Languages</span><h2 id="wheel-name">TypeScript</h2><p id="wheel-description">Typed application code for microservices, developer tooling, and web interfaces.</p></div></div><div class="wheel-aside"><div class="wheel-readout"><span class="wheel-count">01 / 08</span><span id="wheel-state">Locked in</span></div><div class="skill-story-panel" aria-live="polite" aria-atomic="true"><span class="story-label">My experience with</span><h2 id="skill-story-title">TypeScript</h2><p id="skill-story">I use TypeScript across production services and personal projects.</p></div><p id="wheel-help">Drag and let go. A skill clicks into place when the wheel slows down. You can also use the arrow keys or buttons.</p><div class="wheel-controls"><button type="button" data-wheel-step="-1" aria-label="Previous skill">←</button><button type="button" data-wheel-step="1" aria-label="Next skill">→</button></div><a class="text-link" href="#all-skills">See the full list ↓</a></div></div></section><section class="skill-directory section" id="all-skills"><h2>All the tools, in one place.</h2>'''+groups+'</section>'
