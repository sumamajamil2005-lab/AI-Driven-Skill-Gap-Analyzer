def Report_writer(file_path, matched, missing, percentage, level, recommendation, jd_skills):
    """
    Generates a professional text report of the skill gap analysis.
    """
    
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("==========================================\n")
            f.write("        SKILL GAP ANALYSIS REPORT          \n")
            f.write("==========================================\n\n")
            
            f.write(f"OVERALL MATCH: {round(percentage , 2)}%\n")
            f.write(f"CANDIDATE LEVEL: {level}\n")
            f.write(f"ADVICE: {recommendation}\n\n")
            
            f.write("--- ANALYSIS BREAKDOWN ---\n")
            
            # Matched Section
            if matched:
                # ERROR FIX: Pehle names nikaal lo join karne ke liye
                matched_names = [s['name'] for s in matched]
                f.write(f"\n-> MATCHED SKILLS: {', '.join(matched_names)}\n")
                
                # Alag alag breakdown
                full_matches = [s['name'] for s in matched if s['type'] == 'Full']
                partial_matches = [s['name'] for s in matched if s['type'] == 'Partial']
                semantic_matches = [s['name'] for s in matched if s['type'] == 'Semantic']

                f.write("   ∟ FULL MATCH: " + (", ".join(full_matches) if full_matches else "None") + "\n")
                f.write("   ∟ PARTIAL MATCH: " + (", ".join(partial_matches) if partial_matches else "None") + "\n")
                f.write("   ∟ CONCEPTUAL (AI): " + (", ".join(semantic_matches) if semantic_matches else "None") + "\n")
            else:
                f.write("\n-> MATCHED SKILLS: None\n")


            if missing:
                f.write(f"\nMISSING SKILLS: {', '.join(missing)}\n")
            else:
                f.write("\nMISSING SKILLS: None (All requirements met!)\n")
            
            f.write("\n--- JOB SPECIFIC SKILLS ---\n")
            # First 3 skills are consider as primary skills
            primary = jd_skills[:3]
            f.write(f"\n->PRIMARY REQUIREMENTS: {', '.join(primary)}\n")

            f.write("\n------------------------------------------\n")
            f.write("PROFESSIONAL NOTES:\n")
            f.write("- Weighted matching used: Primary skills carry more weight.\n")
            f.write("- Ensure matched keywords appear in your project context.\n")
            f.write("==========================================\n")
            
    except Exception as e:
        print(f"Error writing report: {e}")