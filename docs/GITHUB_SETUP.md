# Quick Start Guide - Git & GitHub Setup

This guide will help you initialize the repository and push it to GitHub.

## Prerequisites

- Git installed on your system
- GitHub account
- Terminal/Command line access

## Step 1: Initialize Git Repository

```bash
# Navigate to project directory
cd /Users/gabrielfallas/Downloads/phishing+websites

# Initialize git repository
git init

# Check status
git status
```

## Step 2: Configure Git (if not already done)

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify settings
git config --global --list
```

## Step 3: Stage and Commit Files

```bash
# Add all files to staging area
git add .

# Commit with a message
git commit -m "Initial commit: Project structure for phishing detection"
```

## Step 4: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the "+" icon in top-right corner → "New repository"
3. Fill in repository details:
   - **Name:** `phishing-detection-pf3325` (or your preferred name)
   - **Description:** "Phishing website detection using Neural Networks - PF3325 Course Project"
   - **Visibility:** Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click "Create repository"

## Step 5: Connect Local Repo to GitHub

```bash
# Add GitHub repository as remote origin
git remote add origin https://github.com/yourusername/phishing-detection-pf3325.git

# Verify remote
git remote -v

# Rename default branch to 'main' (if needed)
git branch -M main
```

## Step 6: Push to GitHub

```bash
# Push to GitHub
git push -u origin main
```

## Step 7: Verify Upload

1. Go to your GitHub repository URL
2. Verify all files and folders are present
3. Check that README.md displays correctly

## Common Commands

### Daily Workflow

```bash
# Check status
git status

# Add changes
git add <file>          # Add specific file
git add .               # Add all changes

# Commit changes
git commit -m "Brief description of changes"

# Push to GitHub
git push

# Pull latest changes (if working in a team)
git pull
```

### Branch Management

```bash
# Create and switch to new branch
git checkout -b feature/new-feature

# Switch between branches
git checkout main
git checkout feature/new-feature

# List all branches
git branch

# Delete a branch
git branch -d feature/old-feature
```

### View History

```bash
# View commit history
git log

# View shortened history
git log --oneline

# View changes
git diff
```

## Troubleshooting

### Authentication Issues

If you encounter authentication problems, you may need to:

1. **Use Personal Access Token (PAT):**
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate new token with 'repo' scope
   - Use token as password when prompted

2. **Use SSH instead of HTTPS:**
   ```bash
   # Change remote URL to SSH
   git remote set-url origin git@github.com:yourusername/phishing-detection-pf3325.git
   ```

### Large Files Warning

If you get warnings about large files:
- Check that `.gitignore` is properly configured
- Models and processed data should NOT be pushed
- Use Git LFS for large files if necessary

### Undo Last Commit

```bash
# Undo last commit but keep changes
git reset --soft HEAD~1

# Undo last commit and discard changes (careful!)
git reset --hard HEAD~1
```

## Best Practices

1. **Commit frequently** with meaningful messages
2. **Pull before push** to avoid conflicts
3. **Use branches** for new features or experiments
4. **Don't commit** large files (models, datasets)
5. **Review changes** before committing: `git diff`
6. **Keep commits atomic** - one logical change per commit

## Useful Git Aliases (Optional)

Add to `~/.gitconfig`:

```ini
[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    unstage = reset HEAD --
    last = log -1 HEAD
    visual = log --graph --oneline --all
```

Usage: `git st` instead of `git status`

## Next Steps

After pushing to GitHub:

1. ✅ Add team members as collaborators (if applicable)
2. ✅ Create project board for tracking tasks (optional)
3. ✅ Set up branch protection rules (optional)
4. ✅ Add topics/tags to repository for discoverability
5. ✅ Update README with actual repository URL

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

**Note:** Replace `yourusername` with your actual GitHub username in all commands.
