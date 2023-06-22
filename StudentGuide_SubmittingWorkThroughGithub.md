Guide for Students: Saving and Submitting Your Work Using Github
========================================================================
Welcome, students! This guide will assist you in leveraging the collaborative power of GitHub for your studies. By following these steps, you will be able to create your own GitHub account, copy ("fork") my (Brendan's) Database-SQL notes repository into your account, and use this personalized copy to save and track your work throughout the course.

Using GitHub in this way gives you a personal space to try out code, experiment with ideas, and make modifications directly in the Jupyter notebooks provided. Importantly, this workspace is linked to the original repository, meaning you can keep your personal repository up to date with the course materials as Brendan makes updates.

In addition to providing a convenient platform for engaging with course materials, this process allows you to familiarize yourself with fundamental concepts and practices in software development. By committing and pushing your changes, you're interacting with Git, a powerful version-control system that's widely used in the tech industry. Pulling updates from the original repository lets you stay in sync with the latest course materials, simulating how developers often work on shared codebases.

By the end of this guide, you will have your own, up-to-date version of these notes, the ability to tailor and experiment with these resources, and a foundational understanding of how software developers use tools like Git and GitHub to collaborate on projects. So let's get started!

1\. Introduction to Git and GitHub
----------------------------------

**Git** is a distributed version-control system that allows multiple people to work on a project without overwriting each other's changes. It tracks changes in any set of files and coordinates work that you and others do simultaneously.

**GitHub**, a web-based platform, provides a place to store your work in the cloud. It adds many of its own features, including simplified version control, easy collaboration with others, issue tracking, and feature requests.

Why is this important for you? As students, using Git and GitHub will help you:

-   Understand the concept of version control and why it's essential in software development
-   Collaborate with others on projects, allowing you to work together without stepping on each other's toes
-   Easily share and showcase your work to others

Let's begin the step-by-step process of interacting with this GitHub repository for Brendan'sDatabase-SQL notes.

2\. Creating a GitHub Account
-----------------------------

Before you can interact with the repository, you'll need a GitHub account. Here's how you can set one up:

1.  Go to [GitHub](https://github.com/).
2.  Click on the 'Sign up' button on the top-right corner.
3.  Fill in your desired username, email address, and password.
4.  Click on the green 'Create account' button.
5.  You'll receive an email to verify your account. Click on the verification link in that email.

3\. Forking the Repository
--------------------------

**Forking** a repository allows you to have a copy of the original repository (in this case, Brendan's Database-SQL notes repository) in your own GitHub account. This allows you to make and save changes without affecting the original repository.

To fork this repository:

1.  Navigate to Brendan's Database-SQL notes repository.
2.  Click on the 'Fork' button at the top-right of the page.
3.  Choose where you want to fork the repository (usually your personal GitHub account).

4\. Cloning and Editing Your Fork
---------------------------------

You now have your own copy of the repository, but it's stored on GitHub's servers. To work on the files locally, you must clone (download) the repository. In general, I recommend using either Google Colab or GitHub Codespaces to complete your work.

### Cloning in Google Colab

Google Colab has a built-in feature to interact with GitHub. Here's how to use it:

1.  Open a new notebook in Google Colab.
2.  Click on 'File' in the top-left corner, then click on 'Open notebook'.
3.  Select the 'GitHub' tab in the pop-up window.
4.  You'll see a field marked 'Enter a GitHub URL or search by organization or user'. Here, input the URL of your forked repository.
5.  Choose the Jupyter notebook you want to work on, and it will open in a new Colab tab.

### Cloning in GitHub Codespaces

GitHub Codespaces provides a complete, configurable dev environment hosted on GitHub. Here's how to set it up:

1.  Navigate to your forked repository.
2.  Click on the green 'Code' button at the top-right of the repository, then choose 'Open with Codespaces'.
3.  Click on the '+ New codespace' button.
4.  This will launch a new codespace where you can work on your code directly in your browser.

5\. Committing and Pushing Changes
----------------------------------

You'll want to save these changes after you've made changes to your Jupyter notebooks. In Git, saving a change is a two-step process: first, you **commit** the change, then you **push** it to GitHub.

### Committing and Pushing in Google Colab

Here's how to do it in Google Colab:

1.  Open the notebook you've been working on.
2.  Go to 'File' > 'Save a copy in GitHub'.
3.  Choose the repository you want to commit to (it should be your forked repository).
4.  Enter a commit message. This message should briefly describe the changes you've made.
5.  Click on 'OK' to commit and push your changes.

### Committing and Pushing in GitHub Codespaces

Here's how to do it in GitHub Codespaces:

1.  Open the notebook you've been working on.
2.  In the left pane, click on the 'Source Control' icon (it looks like a forked branch).
3.  You'll see a list of changes you've made. Enter a commit message in the text field at the top, and press 'Ctrl+Enter' to commit the changes.
4.  To push your changes, go to the '...' menu at the top, then choose 'Push'.

6.\ Submitting Your Work
----------------------------------
Once you've made changes to your own version of the repository (i.e., completed your assignments), you can let Brendan know so he can review your work. This is done via a process called a "pull request." Here's how to do it:

1.  Navigate to your forked repository on GitHub.

2.  Click on 'Pull request' near the top of the repository.

3.  Click on the green 'New pull request' button.

4.  You'll see a comparison between your forked repository (the "head repository") and the original repository (the "base repository"). Ensure you're proposing to merge changes from your repository into my (Brendan's) original repository.

5.  Click on 'Create pull request'.

6.  Give your pull request a title and describe your changes in the comment box. This should include which assignment you're submitting.

7.  Click 'Create pull request' again.

I will then be notified of your pull request and can review your work.


7.\ Updating Your Repository With Brendan's Changes

----------------------------------
I might make updates to the original repository from time to time. To incorporate these updates into your own fork, you'll need to 'pull' these changes. To do this, you can follow these steps:

1.  Navigate to your forked repository on GitHub.

2.  Click on 'Pull request' near the top of the repository.

3.  Click on the link that says "switching the base", which will change the way your pull request works. You'll now merge changes from the original (Brendan's) repository into your forked repository.

4.  Click on 'Create pull request'.

5.  Give your pull request a title and, optionally, a brief description of the changes.

6.  Click 'Create pull request' again.

7.  Assuming no merge conflicts, you can immediately merge the pull request. Click 'Merge pull request', then 'Confirm merge'.

After this, your forked repository will be updated with all the changes from the original repository. Note that this is a workaround: the typical use of pull requests is to propose changes to someone else's repository that they can review and potentially incorporate into their project. In this case, you're using a pull request to update your own forked repository.
