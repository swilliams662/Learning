import numpy
print 2 + 2
SRMP-Mac-004:Python summer$ git add test.py
fatal: not a git repository (or any of the parent directories): .git
SRMP-Mac-004:Python summer$ git commit -m "Created Test File"
fatal: not a git repository (or any of the parent directories): .git
SRMP-Mac-004:Python summer$ git remote -v
fatal: not a git repository (or any of the parent directories): .git
SRMP-Mac-004:Python summer$ git remote add origin https://github.com/swilliams662/Learning.git
fatal: not a git repository (or any of the parent directories): .git
SRMP-Mac-004:Python summer$ git remote -v
fatal: not a git repository (or any of the parent directories): .git
SRMP-Mac-004:Python summer$ pwd
/Users/summer/Dropbox/Python
SRMP-Mac-004:Python summer$ cd Learning
SRMP-Mac-004:Learning summer$ git remote add origin https://github.com/swilliams662/Learning.git
SRMP-Mac-004:Learning summer$ git remote -v
origin	https://github.com/swilliams662/Learning.git (fetch)
origin	https://github.com/swilliams662/Learning.git (push)
SRMP-Mac-004:Learning summer$ git push origin master
error: src refspec master does not match any.
error: failed to push some refs to 'https://github.com/swilliams662/Learning.git'
SRMP-Mac-004:Learning summer$ git remote -v
origin	https://github.com/swilliams662/Learning.git (fetch)
origin	https://github.com/swilliams662/Learning.git (push)
SRMP-Mac-004:Learning summer$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.idea/
	test.py

nothing added to commit but untracked files present (use "git add" to track)
SRMP-Mac-004:Learning summer$ git add test.py
SRMP-Mac-004:Learning summer$ git commit -m "Created Test File"
[master (root-commit) 45176a2] Created Test File
 1 file changed, 2 insertions(+)
 create mode 100644 test.py
SRMP-Mac-004:Learning summer$ git push origin master
Username for 'https://github.com': swilliams662
Password for 'https://swilliams662@github.com':
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/swilliams662/Learning.git/'
SRMP-Mac-004:Learning summer$ git push origin master
Username for 'https://github.com': swilliams662
Password for 'https://swilliams662@github.com':
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 231 bytes | 231.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/swilliams662/Learning/pull/new/master
remote:
To https://github.com/swilliams662/Learning.git
 * [new branch]      master -> master
SRMP-Mac-004:Learning summer$

