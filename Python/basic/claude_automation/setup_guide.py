# 🚀 Complete Setup Guide
# Follow these steps ONE TIME — takes about 30 minutes

# =========================================
# STEP 1: Install Git (if not installed)
# =========================================
# Go to: https://git-scm.com/download/win
# Download and install with default settings
# Then restart your computer

# Verify installation:
# Open Command Prompt and type:
#   git --version
# You should see something like: git version 2.40.0


# =========================================
# STEP 2: Install Python (if not installed)  
# =========================================
# Go to: https://www.python.org/downloads/
# Download latest version
# ⚠️ IMPORTANT: Check "Add Python to PATH" during install

# Verify installation:
#   python --version
# You should see: Python 3.x.x


# =========================================
# STEP 3: Create GitHub Account
# =========================================
# Go to: https://github.com
# Sign up with your email
# Choose a professional username (e.g. yourname-dev)


# =========================================
# STEP 4: Create Your Repo on GitHub
# =========================================
# 1. Click the "+" icon on GitHub → "New repository"
# 2. Name it: python-learning-tracker
# 3. Set it to PUBLIC ✅ (so recruiters can see)
# 4. Check "Add a README file"
# 5. Click "Create repository"


# =========================================
# STEP 5: Clone Repo to Your Computer
# =========================================
# Open Command Prompt in the folder where you want your files
# Run these commands one by one:

git config --global user.name "Your Name"
git config --global user.email "your@email.com"

git clone https://github.com/YOUR_USERNAME/python-learning-tracker.git
cd python-learning-tracker


# =========================================
# STEP 6: Set Up Folder Structure
# =========================================
# Create these folders inside your repo folder:

mkdir basics
mkdir leetcode
mkdir notes
mkdir projects
mkdir .github
mkdir .github/workflows


# =========================================
# STEP 7: Copy the Scripts
# =========================================
# Copy these files into your repo folder:
# - push_old_files.py      (to push your old files)
# - daily_log.py           (your daily 2-minute routine)
# - .github/workflows/daily_tracker.yml  (auto GitHub Actions)


# =========================================
# STEP 8: Push Your Old Files (ONE TIME)
# =========================================
# 1. Copy all your old .py files into the 'basics/' folder
# 2. Open Command Prompt in your repo folder
# 3. Run:

python push_old_files.py

# This will push all old files with their ORIGINAL dates ✅


# =========================================
# STEP 9: Test Your Daily Script
# =========================================
# Run this to test everything works:

python daily_log.py

# It will ask 3 questions → auto commit → show LinkedIn post


# =========================================
# DAILY ROUTINE (after setup)
# =========================================
# Every day after your 4 hours of learning:
#
# 1. Save your code file in basics/ or leetcode/
# 2. Open Command Prompt in repo folder
# 3. Run: python daily_log.py
# 4. Answer 3 questions (2 minutes)
# 5. Copy LinkedIn post → paste on LinkedIn
#
# THAT'S IT! Everything else is automated ✅


# =========================================
# NEED HELP?
# =========================================
# If anything doesn't work, just tell Claude:
# "I got this error: [paste error here]"
# and I'll fix it immediately!