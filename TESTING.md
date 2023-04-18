# Testing - Back to the [README](README.md)

## Python Validation - PEP8
Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files were entered into the online checker and no errors were found in any of the custom codes.

### MovieWarsBlog - blog
* [admin.py](./assets/testme/blog-pep8-admin.png)
* [apps.py](./assets/testme/blog-pep8-apps.png)
* [forms.py](./assets/testme/blog-pep8-forms.png)
* [models.py](./assets/testme/blog-pep8-models.png)
* [tests.py](./assets/testme/blog-pep8-tests.png)
* [urls.py](./assets/testme/blog-pep8-urls.png)
* [views.py](./assets/testme/blog-pep8-views.png)

### MovieWarsBlog - moviewars
* [asgi.py](./assets/testme/moviewars-pep8-asgi.png)
* [settings.py](./assets/testme/moviewars-pep8-settings.png)
* [urls.py](./assets/testme/moviewars-pep8-urls.png)
* [wsgi.py](./assets/testme/moviewars-pep8-wsgi.png)

## Lighthouse
Lighthouse was used to test Performance, Best Practices, Accessibility and SEO. 

* [Lighthouse Results](./assets/testme/lighthouse-results.png)

## HTML Validation
Html code all passed bar this one error that came up saying I used a duplicate ID 5 times in my code but as shown [here.](./assets/testme/html-check-info.png) 
I only use this ID once in my html code. Whihc is only used to style the headings of the blogs on the card body on the homepage.

* [HTML Validation Results](./assets/testme/html-check.png)

## CSS Validation

* [CSS Validation Results](./assets/testme/css-check.png)

## Manual Testing

### Frontend
* The Signup, Login and Logout system has no issues and is working. If you try to submit without filling in inputs django allauth has built in require inputs fild to be filled.
* The Blog posts page is working properly. It display all the blogs.
* If you click on read more it displays the blog details page.
* Back button brings you back to home page when in blog details page.
* If you click on register it brings you too the register form.
* If you click on login it brings you to the login form.
* When logged in nave bar changes and add post and logout is displayed to the user. Also in top right of navbar a message lets the user know they are logged in.
* If you click on add post you can add a new post.
* If you add an image tio the post it will be displayed, if not plaeholder image will be displayed.
* If you click on blog details page you when logged in you now have option to edit or delete a blog.
* In the edit page you can change any of the inputs.
* In the delete page you can delete the selected blog.
* If you want to logout of profile clcik logout and logout. This works fine.
* All the internal links are working and bring the user to the right page on the website.
* All the external links are working and bring the user to the right social media page by opening a new browser tab.
* The drop-down menu when on mobile devices works fine.
* The pagination system is working. It adds another page after 6 posts on the page.
* The CRUD functionality is working without any issues.

### Backend/Admin Panel
* I have tested the Admin Panel repeatedly since the start of the project development and is working wiht no issues.
* All normal functionality is available and working.
* You can post new blogs.
* You can edit blogs.
* You can remove blogs.

## Bugs

* While I was developing the project I tried to add a blog image to my posts but was only displaying the placholder image. By adding an enctype to the form it fixed this issue. 
* While deploying I had major issues wth an etag that wouldnt let me deploy my project to heroku. After a lot of testing and editing a using my last call with my mentor and a long 
time with tutor support to try and fix the issue. I ended up removing django ckeditor from my blog code entirely and the issue has been resolved. And I can now acces my deployed site and no longer get an etag error.