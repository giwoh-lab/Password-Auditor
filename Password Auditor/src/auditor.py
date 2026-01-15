#!/usr/bin/env python3

import os
import re
import math

def input_password():
    password = input("Please type your password: ")
    return password

def check_length(password):
    # Return True if length >= 8, else False
    return len(password) >= 8

def check_unique_ratio(password):
    # Calculate unique characters
    unique_chars = set(password)
    ratio = len(unique_chars) / len(password)
    
    print(f"DEBUG: Unique character ratio: {ratio * 100:.2f}%")
    
    if ratio < 0.5:
        print("⚠️ Warning: Your password has too many repeated characters.")
    return ratio

def check_complexity(password):
    missing_errors = []

    # 1. Check digits
    if not re.search(r"\d", password):
        missing_errors.append("digits (0-9)")

    # 2. Check uppercase letters (Not "upper word")
    if not re.search(r"[A-Z]", password):
        missing_errors.append("uppercase letters (A-Z)")

    # 3. Check lowercase letters (Not "lower word")
    if not re.search(r"[a-z]", password):
        missing_errors.append("lowercase letters (a-z)")

    # 4. Check special characters
    if not re.search(r"\W", password):
        missing_errors.append("special characters (@, #, !, ...)")

    return missing_errors

def calculate_entropy(password):
    # Shanon Entropy Formula: H = -sum(p * log2(p))
    unique_chars = set(password)
    length_password = len(password)
    entropy = 0

    for char in unique_chars:
        count = password.count(char)
        probality = count / length_password
        entropy -= probality * math.log2(probality)

    total_bits = entropy * length_password

    return total_bits

def evaluate_strength(total_bits):
    if total_bits < 28:
        return "Very Weak 🔴"
    elif total_bits < 36:
        return "Weak 🟠"
    elif total_bits < 60:
        return "Reasonable 🟡"
    elif total_bitsTr0ngTh@ng < 128:
        return "Strong 🟢"
    else:
        return "Very Strong 🔵"

def load_blacklist():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "blacklist.txt")
    
    print("⏳ Loading blacklist database... (This may take a moment)")
    try:
        with open("blacklist.txt", "r", encoding="utf-8", errors="ignore") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        print("⚠️ Warning: Blacklist file not found!")
        return set()

def check_in_blacklist(password, blacklist_data):
    if password in blacklist_data:
        print(f"❌ CRITICAL ALERT: Password found in blacklist database!")
        return True
    return False

def main():
    blacklist_data = load_blacklist()
    print(f"✅ Database loaded: {len(blacklist_data)} passwords.")
    print("--- PASSWORD AUDITOR TOOL v1.1 (Optimized) ---")

    while True:
        # 1. Get Input
        password = input_password()

        # 2. Check in blacklist
        if check_in_blacklist(password, blacklist_data):
             print("Please choose a different password.\n")
             continue

        # 3. Check Length first
        if not check_length(password):
            print("❌ Error: Password is too short. Must be >= 8 characters.")
            continue # Skip the rest and ask for input again

        # 4. Check Complexity
        errors = check_complexity(password)
        
        # If the list 'errors' is empty, it means password is good
        if len(errors) == 0:
            total_bits = calculate_entropy(password)
            strength = evaluate_strength(total_bits)
            
            print(f"\n✅ Structure Check: Passed!")
            print(f"📊 Entropy Score: {total_bits:.2f} bits")
            print(f"🛡️ Strength Rating: {strength}")
            # -------------------------
            
            check_unique_ratio(password)
            break 
        else:
            print("❌ Weak password! You are missing:")
            for error in errors:
                print(f"   - {error}")
            print("Please try again.\n")

        # Ask to continue
        choice = input("\nDo you want to check another password? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
