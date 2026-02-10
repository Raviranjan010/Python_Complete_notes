# ---------------------------------------------------------
# Topic: Variable Scope (Local vs Global)
# File: scope.py
# ---------------------------------------------------------

# Global Variable
score = 0

def show_score():
    # Can access global variable
    print(f"Current Score: {score}")

def update_score_wrong():
    # score += 10 
    # ERROR UnboundLocalError: local variable 'score' referenced before assignment
    pass

def update_score_right():
    global score # Using global keyword
    score += 10
    print(f"Score updated to: {score}")

def local_scope_demo():
    hero = "Batman" # Local variable
    print(f"Hero inside: {hero}")

# --- Execution ---
show_score()
update_score_right()
show_score()

local_scope_demo()
# print(hero) # Error: 'hero' is not defined

# ==========================================
# Exam Trick: Nested Scope & Global
# ==========================================
print("\n--- Exam Trick: Nested Scope ---")
c = 31

def school():
    a = 30
    b = 23
    c = a + b # Local 'c' to school()

    def Class():
        global c # Refers to the GLOBAL c (31), not school's c
        print(f"Inside Class (Global): {c}")
        c = 7 # Modifies LOCAL 'c' if not global, but here modifies GLOBAL

    Class()
    print(f"Inside School (Local): {c}") # Prints school's local c

school()
print(f"Global c after execution: {c}")
