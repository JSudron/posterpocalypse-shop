## Developer Tools

### Google Chrome Dev Tools

- Used to test the responsiveness of the website.
- Used to make on the fly changes to the css to alter the design of the site.
- Debugging of the javascript as errors are easily identified in the console.

### Responsinator

- Used to view to how the site looks on a wide range of screen sizes at once.

## Validation Tools

### Validator W3

- The only errors shown were warnings about using too many hyphens in the comments.
- Amended this by having only too hyphens before and after a comment.

### Jigsaw W3

- Used to validated the CSS code. Numerous errors were found but these were within the scripts loaded at the beginning of the page.
- Within my custom CSS `-webkit` properties were identified as invalid but this was ignored.

### JSHint 

- The following issues were found when validating the Javascript code, all issues were fixed.
- `$ is unused variable`
- This was ignored.

### Esprima Syntax Validator

- Used to validate the Javascript. No errors were found.

### Pep8 Online Validator

- Used to validate the Python syntac. No errors were found.

## Manual Tests

- An initial 'test.py' file was created to make sure that python was connecting up correctly.
- The live web address was tested on a variety of web browsers: Chrome/Safari/Opera/Explorer.
- Each link on the site was tested to ensure it linked to the correct place.
- The story 'The Impossible' was added using the Add Stories page.
- Each part of the story was then edited to ensure changes occurred correctly.
- A 'Test' story was added which was then deleted to test the delete function.
- The Submit Story form was deleted to ensure that each field was required to submit. 

## Peer-Code Review

- Once the website was complete it was submitted to my peers for review.
- It was suggested to change the width on navbar & hero-image to 100% instead of 100vw as this was creating oveflow-x issues.
- The script link was changed to src instead of href as is the standard practice.
- Height of hero-image was changed to 120vh for smaller devices to ensure no overlapping.