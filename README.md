How to run?
===========

In the command prompt type:

    python hasip/hasip.py <arguments>

Development
===========

Getting started
---------------

* Fork the project (click the "Fork" button on the project home)
* The project gets now forked to your own namespace at gitlab instance with the state of code during the time you forked the project.
* In your namespace you can now see a fork of the porject.
* Clone it to your workspace by executing the following commands:

```
# Change to your working directory
cd ~/YOUR_WORKSPACE_DIRECTORY
# Clone the repository from your fork
git clone git@github.com:YOUR_USERNAME/hasip.git hasip
# change to cloned fork
cd hasip
# Adding the upstream to fetch the newest code
git remote add upstream git@github.com:thehasip/hasip.git
```

* You now have successful set up your initial project.
* To start coding proceed as described bellow

```
git fetch upstream  # get the latest refs from upstream project
git pull upstream master # get the latest code from upstream
git checkout -b YOUR_BRANCH_NAME # create a branch for the feature/bug/whatever you are willing to work on
<start hacking>
git push origin YOUR_BRANCH_NAME
```

* To get your branch into the main repositry create a "Merge request" via the webinterface.

Before pusing:
--------------

* Use good commit message
* Files which belongs togehter should be all within one commit
* Do not push/merge with master without haven checked thsi with some other developer

Problems with git?
==================

Check out the excellent documentation at: [git-scm.com](http://git-scm.com/documentation)
