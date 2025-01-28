# my-first-repo
For 11-12SE: A beginner-friendly repository with a number-guessing game.


# GitHub for Dummies

## 1-Hour GitHub and Hosting Lesson Plan
This lesson introduces students to GitHub, guides them through creating and publishing a simple number-guessing game, and teaches them how to host it live using GitHub Pages.

## Lesson Outline
- **Introduction to GitHub (10 minutes)**
- **Creating a Repository (10 minutes)**
- **Building and Uploading a Number-Guessing Game (20 minutes)**
- **Hosting on GitHub Pages (15 minutes)**
- **Wrap-Up and Homework (5 minutes)**

## Lesson Details

### 1. Introduction to GitHub (10 minutes)
**Explain the basics:**
- A platform for sharing and managing code online.
- Tracks changes to your projects and helps with collaboration.

**Show an example:**
- Visit your profile ([Mr. Zamora’s GitHub](https://github.com/Mr-Zamora)) to demonstrate how repositories work.

**Key terms:**
- Repository: A folder for your project.
- Commit: A saved change.
- Push: Upload changes to GitHub.
- Fork: Create a personal copy of a project.

### 2. Creating a Repository (10 minutes)
**Step-by-step instructions:**
- Log in to GitHub.
- Click the New Repository button.
- Fill in:
  - Repository Name: `my-first-repo`.
  - Description: `A beginner-friendly repository with a number-guessing game.`
- Click Create Repository.

**Outcome:** Students will see their first repository page with a `README.md` file.

### 3. Building and Uploading a Number-Guessing Game (20 minutes)
**Step 1: Copy the HTML Code**
Provide the following game code for students to copy:

```python
# guess_number.py
# A simple game for practising GitHub basics
# Fork this repo, modify the game, and have fun!

import random

def guess_the_number():
    """A simple number-guessing game."""
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    number = random.randint(1, 10)  # Random number between 1 and 10
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game if this script is executed directly
if __name__ == "__main__":
    guess_the_number()
```

**Step 2: Upload the File to GitHub**
- In the repository, click Add file > Create new file.
- Name the file `guess_number.py`.
- Paste the code into the editor.
- Add a commit message: `Added guess_number.py game`.
- Click Commit new file.

### 4. Hosting on GitHub Pages (15 minutes)
**Step-by-step instructions:**
- Go to the repository settings and scroll to the Pages section.
- Under Source, select the branch with your file (usually `main`) and click Save.
- GitHub will provide a URL (e.g., `https://mr-zamora.github.io/my-first-repo/`).
- Test the URL to ensure the game is live.

**Optional: Make `index.html` the default page**
- Use my `index.html` and put it in your repo.
- Revisit your own GitHub Pages URL to confirm it loads automatically.

### 5. Wrap-Up and Home learning (5 minutes)
**Summary:**
- Students learned to:
  - Use GitHub for creating repositories and uploading files.
  - Build a simple number-guessing game.
  - Host their project online with GitHub Pages.

- Home learning
  - Fork this repo.
  - How? https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
 


