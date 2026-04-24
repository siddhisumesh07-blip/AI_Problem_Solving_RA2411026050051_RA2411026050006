import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# --- PROBLEM 16: AI CHATBOT LOGIC ENGINE (UNIFICATION) ---
def chatbot_logic_engine():
    print("\n--- Problem 16: AI Chatbot Logic Engine ---")
    # Knowledge base using formal logic patterns as per instruction sheet
    knowledge_base = {
        "process_order(ITEM)": "Action: Validating ITEM in inventory...",
        "check_status(ID)": "Action: Retrieving status for ID...",
        "get_info(TOPIC)": "Action: Searching database for TOPIC..."
    }
    
    print("Available Patterns: process_order(X), check_status(X), get_info(X)")
    user_query = input("Enter logic query (e.g., process_order(Laptop)): ").strip()
    
    matched = False
    # Unification Algorithm Implementation
    for pattern, action in knowledge_base.items():
        p_func = pattern.split('(')[0]
        if user_query.startswith(p_func) and '(' in user_query and ')' in user_query:
            # Extract the constant to unify with the variable
            extracted_val = user_query.split('(')[1].replace(')', '')
            
            print(f"\n[Unification Successful]")
            print(f"Goal: {pattern}")
            print(f"Fact: {user_query}")
            print(f"Substitution: {{ Variable: {pattern.split('(')[1].replace(')', '')}, Value: {extracted_val} }}")
            print(f"Result: {action.replace(pattern.split('(')[1].replace(')', ''), extracted_val)}")
            matched = True
            break
            
    if not matched:
        print("Unification Failed: Query does not match any known logic rules.")

# --- PROBLEM 18: STUDENT PERFORMANCE PREDICTOR ---
def performance_predictor():
    print("\n--- Problem 18: Student Performance Predictor ---")
    # Dataset with 4 variables as required by Image 5
    # (Hours Studied, Attendance, Previous Marks, Resources Accessed)
    data = {
        'Hours_Studied': [2, 5, 8, 1, 7, 4, 9, 3, 6, 2],
        'Attendance': [60, 80, 95, 50, 85, 75, 98, 70, 88, 55],
        'Prev_Marks': [40, 65, 85, 30, 80, 60, 95, 55, 82, 45],
        'Resources': [1, 3, 5, 1, 4, 2, 6, 2, 4, 1],
        'Final_Grade': [45, 68, 88, 35, 82, 62, 96, 58, 85, 48]
    }
    df = pd.DataFrame(data)
    X = df[['Hours_Studied', 'Attendance', 'Prev_Marks', 'Resources']]
    y = df['Final_Grade']
    
    # Train Linear Regression Model
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    
    print(f"\nModel Evaluation Metrics:")
    print(f"R-Squared Score: {r2_score(y, y_pred):.4f}")
    print(f"Mean Squared Error: {mean_squared_error(y, y_pred):.2f}")
    
    print("\n--- Predict Performance ---")
    try:
        h = float(input("Enter Hours Studied: "))
        a = float(input("Enter Attendance %: "))
        p = float(input("Enter Previous Marks: "))
        r = float(input("Enter Resources Accessed: "))
        
        result = model.predict([[h, a, p, r]])
        print(f"Predicted Final Grade: {result[0]:.2f}")
    except ValueError:
        print("Error: Please enter numerical values.")

# --- MAIN MENU ---
if __name__ == "__main__":
    while True:
        print("\n" + "="*30)
        print("MEMBER 2: PROJECT SUBMISSION")
        print("="*30)
        print("1. Problem 16: Chatbot Logic (Unification)")
        print("2. Problem 18: Performance Predictor (Regression)")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        if choice == '1':
            chatbot_logic_engine()
        elif choice == '2':
            performance_predictor()
        elif choice == '3':
            print("Closing member2.py...")
            break
        else:
            print("Invalid input. Select 1, 2, or 3.")
