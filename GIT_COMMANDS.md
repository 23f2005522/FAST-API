# Git Commands Cheatsheet

A practical reference to get comfortable with Git — everyday commands, branches, undo, remotes/origin, and daily workflows.

---

## Everyday Basics

```bash
git status                 # what’s changed?
git add <file>             # stage one file
git add .                  # stage everything
git commit -m "message"    # save a snapshot
git log --oneline          # short commit history
git diff                   # unstaged changes
git diff --staged          # staged changes
```

---

## Sync with Remote (GitHub)

```bash
git clone <url>            # download a repo
git remote -v              # see remotes
git pull                   # fetch + merge latest
git fetch                  # download updates (don’t merge)
git push                   # upload your commits
git push -u origin HEAD    # first push of a new branch
```

---

## Branches

```bash
git branch                 # list local branches
git branch <name>          # create branch
git switch <name>          # switch branch (newer)
git checkout <name>        # switch branch (classic)
git switch -c <name>       # create + switch
git merge <branch>         # merge into current branch
git branch -d <name>       # delete merged branch
```

---

## Undo / Fix Mistakes (safe → stronger)

```bash
git restore <file>         # discard unstaged file changes
git restore --staged <file># unstage (keep edits)
git reset HEAD~1           # undo last commit, keep files
git commit --amend         # fix last commit message/files

# avoid unless you know why:
git reset --hard HEAD      # throw away local changes
```

---

## Inspect History

```bash
git log                    # full history
git log --oneline --graph  # visual branch history
git show <commit>          # one commit details
git blame <file>           # who changed each line
```

---

## Stash (pause work)

```bash
git stash                  # save dirty work temporarily
git stash list
git stash pop              # restore + remove stash
git stash apply            # restore, keep stash
```

---

## Working with Origin / Remotes

### See remotes

```bash
git remote                 # list remote names
git remote -v              # names + fetch/push URLs
git remote show origin     # full details for origin
```

### Add origin

```bash
# HTTPS
git remote add origin https://github.com/USERNAME/REPO.git

# SSH
git remote add origin git@github.com:USERNAME/REPO.git
```

### Change / update origin URL

```bash
git remote set-url origin https://github.com/USERNAME/NEW-REPO.git
git remote -v              # verify
```

### Rename a remote

```bash
git remote rename origin upstream
```

### Remove origin

```bash
git remote remove origin
# same thing:
git remote rm origin
```

### Push / pull with origin

```bash
git push -u origin main        # first push; sets upstream
git push                       # later pushes (after -u)
git pull origin main           # pull a specific branch
git fetch origin               # download updates only
git fetch origin --prune       # also drop deleted remote branches
```

### Wrong origin → fix

```bash
git remote -v
git remote remove origin
git remote add origin https://github.com/USERNAME/CORRECT-REPO.git
git remote -v
git push -u origin main
```

### Origin quick reference

| Goal | Command |
|------|---------|
| Check origin | `git remote -v` |
| Details | `git remote show origin` |
| Add | `git remote add origin <url>` |
| Change URL | `git remote set-url origin <url>` |
| Remove | `git remote remove origin` |
| Rename | `git remote rename origin <newname>` |
| First push | `git push -u origin main` |

> **Tip:** `origin` is just the usual name for your main remote. You can have others too (`upstream`, `fork`, etc.).

---

## Typical Daily Flow

```bash
git status
git pull
# ... edit files ...
git add .
git commit -m "explain why, not what"
git push
```

---

## Feature-Branch Flow

```bash
git switch main
git pull
git switch -c feature/ml-predict
# ... work ...
git add .
git commit -m "add /predict endpoint"
git push -u origin HEAD
# then open a PR on GitHub
```

---

## Memorize These First (Top 10)

| Command | Why |
|---------|-----|
| `git status` | Always start here |
| `git add .` | Stage changes |
| `git commit -m "..."` | Save snapshot |
| `git pull` | Get latest |
| `git push` | Share work |
| `git log --oneline` | See history |
| `git switch -c <name>` | New branch |
| `git diff` | Review before commit |
| `git restore <file>` | Undo file edits |
| `git stash` / `pop` | Pause unfinished work |

---

## Mini Practice

```bash
cd d:\FASTAPI
git status
git add Readme.md
git commit -m "add FastAPI learning roadmap"
git log --oneline
```

---

## First-Time Repo Setup (local → GitHub)

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```
