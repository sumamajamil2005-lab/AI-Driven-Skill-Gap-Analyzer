from matcher.ai_matcher import get_embeddings , is_semantic_match


_SKILL_NORMALIZATION = {
    # Data Science & AI
    "machine learning": "ml",
    "ml": "ml",
    "artificial intelligence": "ai",
    "ai": "ai",
    "natural language processing": "nlp",
    "nlp": "nlp",
    "deep learning": "dl",
    "dl": "dl",
    "computer vision": "cv",
    "cv": "cv",
    "generative ai": "genai",

    # Cloud & DevOps
    "kubernetes": "kubernetes",
    "k8s": "kubernetes",
    "amazon web services": "aws",
    "aws": "aws",
    "google cloud platform": "gcp",
    "gcp": "gcp",
    "microsoft azure": "azure",
    "azure": "azure",
    "continuous integration": "ci/cd",
    "continuous deployment": "ci/cd",
    "ci/cd": "ci/cd",
    "dockerization": "docker",
    "docker": "docker",

    # Frontend & Backend
    "javascript": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "ts": "typescript",
    "python": "python",
    "py": "python",
    "reactjs": "react",
    "react.js": "react",
    "react": "react",
    "django rest framework": "drf",
    "drf": "drf",
    "nodejs": "node.js",
    "node": "node.js",
    "node.js": "node.js",

    # Databases & Tools
    "structured query language": "sql",
    "sql": "sql",
    "mysql": "sql",
    "postgresql": "sql",
    "postgres": "sql",
    "mongodb": "nosql",
    "mongo": "nosql",
    "nosql": "nosql",
    "version control": "git",
    "git": "git",
    "visual studio code": "vscode",
    "vscode": "vscode",
    "container orchestration": "kubernetes",
    "automated deployment": "ci/cd",
    "ci/cd" : "automated deployment",
    "kubernetes" : "container orchestration",
    "python": "backend",
    "flask": "backend",
    "fastapi": "backend",
    "mysql": "database",
    "postgresql": "database",
    "relational databases": "database",
    "azure": "cloud",
    "gcp": "cloud",
    "microsoft cloud": "cloud",
    "Microsoft Cloud" : "azure",
    "microservices": "distributed architecture",
    "independent services": "microservices",
    "terraform": "infrastructure as code",
    "ansible": "infrastructure as code",
    "kubernetes": "orchestration",
    "helm charts": "orchestration",
    "dynamodb": "nosql",
    "cassandra": "nosql",
    "hive": "big data"
}

def _normalize(skill):
    """Converts common abbreviations and long forms to standard keywords."""
    skill = skill.lower().strip()
    return _SKILL_NORMALIZATION.get(skill, skill)


def skill_matcher(jd_skills , resume_skills):
    if not jd_skills or not resume_skills:
        print("\nInvalid input! ")
        return []
    
    missing_skills = []
    matched_skill = []
    earned_points = 0
    total_points = 0
    
    normalized_resume = [_normalize(s) for s in resume_skills]
    normalized_jd = [_normalize(j) for j in jd_skills]

    res_emb= get_embeddings(normalized_resume)
    jd_emb = get_embeddings(normalized_jd)

    lower_resume = [s.lower() for s in resume_skills]

    
    for index , skill in enumerate(jd_skills):
        weight = 2 if index < 3 else 1
        total_points += weight


        if skill.lower() in lower_resume:
            matched_skill.append(skill)
            earned_points += weight
            continue


        if normalized_jd[index] in normalized_resume:
            matched_skill.append(skill)
            earned_points += weight
            continue



        
        if is_semantic_match(jd_emb[index] , res_emb):
            matched_skill.append(skill)
            earned_points += weight
            continue
        else:
            missing_skills.append(skill)

    match_percentage = float((earned_points / total_points) * 100) if total_points > 0 else 0
    return matched_skill , missing_skills , match_percentage