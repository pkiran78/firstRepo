This is file in first repo

    It tests area of rectangle

Git Commands

    echo "# firstRepo" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote remove origin
    git remote add origin https://github.com/pkiran78/firstRepo.git
    git push -u origin main

Git command to push changes to branch:

	git checkout -b newBranch main
	Make changes to file
	git add <File-name>
	git commit -m "message"
	git push origin newBranch
	
Git commands for merging

	Perform changes to newBranch, check git status
	Go to main branch using: git checkout main
	Pull latest changes using: git pull --rebase
	Come back to newBranch using: git checkout newBranch
	Move newBranch changes to stash using: git stash
	Merge latest changes of main to newBranch using: git merge main
	Now you have latest changes in newBranch
	Apply your previous changes using: git stash pop
	Now, if conflict occurs, remove it manually.After removing conflict you can not do git stash then do -> git reset HEAD <file_on_conflict>
	Add changes using: git add <file-name>
	Commit changes: git commit
	Push: git push origin newBranch
	Pull request using UI.
