def mental_health_check():
    
    print("Hello! I will ask a few questions to check your mental health status.")
    
    topics = [
        "Energy levels",
        "Sleep quality",
        "Stress levels",
        "Mood",
        "Physical health",
        "Work-life balance",
        "Self-esteem",
        "Overall satisfaction with life",
        "Diet and nutrition",
    ]
    
    questions = [
        f"On a scale of 1 to 5, how would you rate your {topic}?" for topic in topics              
    ]
    
    total_score = 0
    for question in questions:
        while True :
            
            try:
                score = float(input(question + " "))
                if 1 <= score <= 5:
                    total_score += score
                    break
            
            except ValueError:
                print("Invalid input.")
                
    category = ""          
    avg_score = total_score / len(questions)
    
    print(f"YOUR AVERAGE SCORE IS: {avg_score:.2f}")
    
    if avg_score >= 4:
        category = "Healthy"
        print("Your mental health status is:", category)
        print("You seem healthy, continue taking good care of yourself and maintain a balanced lifestyle.")
        
    elif avg_score >= 3:
        category = "Moderately Healthy"
        print("Your mental health status is:", category)
        print("You look healthy but you can still improve your mental health by taking care of yourself and maintaining a balanced lifestyle.")
        
    elif avg_score >= 2:
        category = "need to improve"
        print("Your mental health status is:", category)
        print("You overthink and need to calm your mind and take care of yourself.")
        
    else:
        category = "stressed"
        print("Your mental health status is:", category)
        print("You are struggling to stay happy and really need to take good care of yourself and seek support if needed.")
        
if __name__ == "__main__":    
    mental_health_check()
    
                