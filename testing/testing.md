## Developer Tools

### Google Chrome Dev Tools

- Used to test the responsiveness of the website.
- Used to make on the fly changes to the css to alter the design of the site.
- Debugging of the javascript as errors are easily identified in the console.

### Responsinator

- Used to view to how the site looks on a wide range of screen sizes at once.

## Validation Tools

### Validator W3

1. 
- Warning: The type attribute is unnecessary for JavaScript resources.
- `<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/emailjs-com@2.4.1/dist/email.min.js">`
- Ignored in the case as provides easier readability

2. 
- Error: An img element must have an alt attribute, except under certain conditions.
- `<img class="navbar-brand" src="https://github.com/JSudron/posterpocalypse-shop/blob/36d120412fa1dbb3bdb9793b93bf332e4bb73360/media/images/logo-small.jpg?raw=true">`
- Added alt element to the image.

3. 
- Element form not allowed as child of element ul in this context
- `<form class=" mb-3 mx-auto">`
- Wrapped the form in a li item.

### Jigsaw W3

- Used to validated the CSS code. Numerous errors were found but these were within the scripts loaded at the beginning of the page.
- Within my custom CSS `-webkit` properties were identified as invalid but this was ignored.
- Some issues with background-colour & colour of buttons being the same but these were ignored as code is working as intended visually.

### JSHint 

- The following issues were found when validating the Javascript code, all issues were fixed.
- `$ is unused variable`
- This was ignored.

### Esprima Syntax Validator

- Used to validate the Javascript. No errors were found.

### Pep8 Online Validator

- Used to validate the Python syntax. No errors were found.

### Django Validation

- Manual validators were created for the vast majority of django apps.
- However, due to time contsraints 100% validation ws not obtained.

## Manual Tests

- An initial 'test.py' file was created to make sure that python was connecting up correctly.
- The live web address was tested on a variety of web browsers: Chrome/Safari/Opera/Explorer.
- Each link on the site was tested to ensure it linked to the correct place.
- Products were edited in the admin section to ensure changes were made on the site.
- Test payments were made for the products.

## Mentor Review

- Once the website was complete it was submitted to my mentor for review.
- He recommended making the checkout button larger & moving the search bar to the categories section on products.html.
- These changes were implemented.