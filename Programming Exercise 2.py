# Spam Detector Program
# COP2373

def get_spam_keywords():
    """
    Returns a list of common spam keywords and phrases.
    """
    keywords = [
        "free", "winner", "congratulations", "urgent", "act now",
        "limited time", "click here", "risk free", "earn money",
        "make money fast", "guaranteed", "no obligation",
        "exclusive deal", "claim now", "credit card",
        "loan approval", "pre-approved", "cheap", "discount",
        "buy now", "double your income", "work from home",
        "investment opportunity", "get paid",
        "no experience required", "special promotion",
        "call now", "verify your account",
        "password reset", "free gift"
    ]
    return keywords


def calculate_spam_score(message, keywords):
    """
    Scans the message for spam keywords and calculates spam score.
    Returns score and list of found keywords.
    """
    score = 0
    found_words = []

    message = message.lower()

    for word in keywords:
        occurrences = message.count(word)
        if occurrences > 0:
            score += occurrences
            found_words.append(word)

    return score, found_words


def determine_spam_likelihood(score):
    """
    Determines spam likelihood based on score.
    """
    if score == 0:
        return "Very unlikely to be spam."
    elif score <= 3:
        return "Low likelihood of spam."
    elif score <= 6:
        return "Moderate likelihood of spam."
    else:
        return "High likelihood of spam."


def main():
    print("=== Spam Detector Program ===")
    message = input("Enter the email message to analyze:\n")

    keywords = get_spam_keywords()
    score, found_words = calculate_spam_score(message, keywords)
    likelihood = determine_spam_likelihood(score)

    print("\n--- Results ---")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")

    if found_words:
        print("Spam words/phrases detected:")
        for word in found_words:
            print("-", word)
    else:
        print("No spam keywords detected.")


if __name__ == "__main__":
    main()
