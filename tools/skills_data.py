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

def render_skills():
    from html import escape
    categories = ''.join(f'<button type="button" data-skill-category="{escape(category)}" aria-pressed="{str(i == 0).lower()}">{escape(category)}</button>' for i,category in enumerate(SKILLS))
    groups = ''.join('<section class="skill-directory-group"><h2>'+escape(category)+'</h2><div class="skill-directory-grid">'+''.join(f'<article data-skill="{escape(name, quote=True)}" data-skill-group="{escape(category, quote=True)}"><h3>{escape(name)}</h3><p>{escape(description)}</p></article>' for name,description in items)+'</div></section>' for category,items in SKILLS.items())
    return '''<section class="skills-explorer" aria-label="Interactive skills wheel"><div class="skill-categories" role="group" aria-label="Choose a skill category">'''+categories+'''</div><div class="wheel-layout"><div class="skill-wheel"><div class="wheel-ring"></div><div class="wheel-ring inner"></div><div class="wheel-rotor" id="wheel-rotor"></div><div class="wheel-center" aria-live="polite" aria-atomic="true"><span id="wheel-category">Languages</span><h2 id="wheel-name">TypeScript</h2><p id="wheel-description">Typed application code for microservices, developer tooling, and web interfaces.</p></div></div><div class="wheel-aside"><span class="wheel-count">01 / 08</span><h2>A closer look<br>at my stack.</h2><p>Pick a category, then a skill.<br>Use the arrows to turn the wheel.</p><div class="wheel-controls"><button type="button" data-wheel-step="-1" aria-label="Previous skill">←</button><button type="button" data-wheel-step="1" aria-label="Next skill">→</button></div><a class="text-link" href="#all-skills">See the full list ↓</a></div></div></section><section class="skill-directory section" id="all-skills"><h2>All the tools, in one place.</h2>'''+groups+'</section>'
