[![Build Status](https://travis-ci.org/JSudron/posterpocalypse-shop.svg?branch=master)](https://travis-ci.org/JSudron/posterpocalypse-shop)

# POSTERPOCALYPSE - Project Four: Full Stack Development

![Screenshot](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/posterpocalypse-mockup.jpg?raw=true)

A live demo can be found [here](https://posterpocalypse.herokuapp.com/).

## Introduction - Project Purpose

For this project I was tasked with creating a website/app utilising the full range of full stack development skills I've currently learnt. 
I was required to utilise Django along with a postgres database along with other coding language. The app is an online shop which stocks limited edition screen printed posters.
The app is actually designed for a business that I previously ran but due to time contraints couldn't keep up to date. Over the past 10 years I've collected a large collection of 
limited-edition screen-printed posters. Due to the limited amount of posters printed the market for selling these on is quite lucrative, however this is predominantly done on eBay.
Given the charges & other restraints eBay poses I'm looking to create my own online shop to sell the artwork.

## UX
 
### Goals

To allow users to view & purchase limited edition artwork.

#### Target Audience

- Users whom speak English as currently this is the only language catered for.
- Gallery owners.
- Fans of popular movie, tv & music.
- Artwork lovers.
- Users whom like to shop online.

### User Stories

#### As a Store Owner I want to...

- Have an attractive & fast website so it will keep users engaged.
- Provide a pleasant user experience so users continue to visit the site.
- Enable users to easily view & search for limited edition artwork so they will make purchases.
- Provide income with the sale of artwork so I can buy further inventory & expand the shop.
- In the future be able to advertise & support local artists so that I can appeal to & support my community.
- Allow users to contact the site should they have any enquiries so I can keep them happy & gain positive feedback.
- Be able to easily update the shop with new products so users can purchase them.
- Ensure all payments & customer details are secure so customers feel safe shopping at my store.

#### As a UX Designer I want to...

- Track user behaviour so I can continue to enhance the user's experience.
- Provide a website which is attractive, yet can easily be modified so the owner can make changes if required.
- Ensure the functionality of the website provides the results required by the user so they continue to use the site.
- Provide a means for the user to contact the shop so any issues are directed to the owner rather than elsewhere.
- Ensure all payments & customer details are secure so the customer & owner feel safe using the site.

#### As a Customer I want to...

- Shop for a variety of artwork online so I can buy pretty things for my home.
- Be able to easily contact the shop so I can direct any issues or enquiries directly to them & get the feedback I need.
- Can search for previous orders I've made so I can see what I've bought & how much I've spent.
- Update any details I've stored so I know the orders will get delivered where I need them to.
- Ensure all payments & details stored are secure so I feel safe buying things on the store.
- View FAQ such as return & refund policies so I know of the policies before making a purchase.
- Login & register to my own account on the site so I can keep track of previous orders & store my details so purchasing products is easier.

### Design

#### Colours

- #f000ff Magenta
- #8c8b8b Suva Grey
- #78FE45 Screamin' Green
- #fff White

The website [Coolors](https://coolors.co/) was used to find an attractive colour scheme which evokes a simple yet retro/comic style.
Neon colours were used to used contrasts against the white & suva grey which providing colourful pops against the simple design. 
The colours are clean & simple but also provide a bit of an attitude. 

#### Fonts

- Bangers

The font was found on the site [Google Fonts](https://fonts.google.com/). 
Bangers was chosen as it wasn't your average plain text. It has a comical element, whilst also mimicing the style often found on movie posters.
Adds some edge to the app whilst also having great readbility.

#### Logo & Jumbotron

- The logo was created in Photoshop along with the Jumbotron image.
- Both were created with the Zombie Fonts pack purchased from [The Hungry Jpeg](https://thehungryjpeg.com/product/3653176-zombie-fonts-melt).
- Used as gives a cool retro look in keeping with the products being sold.

### Wireframes

- All wireframes were created using Balsamiq 3 software.
- The wireframes display the original concepts for the site, however these changed due to striving to provide an enhanced user experience but occasionly due to coding/time constraints.

- [Home](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Home.png?raw=true).

- [Register](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Register.png?raw=true).

- [Login](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Login.png?raw=true).

- [My Account](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/My%20Account.png?raw=true).

- [Update Personal](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Update%20Personal.png?raw=true).

- [Update Address](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Update%20Address.png?raw=true).

- [Update Password](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Update%20Password.png?raw=true).

- [Products](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Products.png?raw=true).

- [Selected Product](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Selected%20Product.png?raw=true).

- [Cart](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Cart.png?raw=true).

- [Checkout](https://github.com/JSudron/posterpocalypse-shop/blob/master/media/images/mockups/Checkout.png?raw=true).

## Features/Functionality

### Elements Present On Each Page

#### Navigation Bar 

- Has an alert bar stating free delivery is available.
- The Navbar-brand is situated above the navbar, with the image of the shop's logo used rather than html text.
- Includes a search bar so customers can search for products by name.
- The cart link displays the number of items in the cart.
- A collapsible menu is used, opted for text 'MENU' rather than a hamburger menu as a menu toggle.


#### Footer 

- Fixed to the bottom of the page has a copyright declaration.
- Provides links to social media.
- Provides links to various pages on the site & provides relevant account links depending on whether user is signed in.

### Apps Within the Site

#### Home

- Large jumbotron image created in Photoshop with stylish melted effect.
- Includes about page which includes details of the shop along with FAQs such as the returns & refund policy.
- Includes contact page which has a contact form so customers can contact the site owners.

#### Account

- Registration & login pages which require e-mail & password input.
- Pages which allow the user to reset their password if forgotten.
- Profile page which has the user shipping details which can be update if required.
- The profile page also has access toa page which displays the customer's previous pages.

#### Products 

- Displays 8 products per page with pagination.
- Categories are displayed above the products allowing the customer to filter the products by category or view all products.
- Each product has a product detail page which includes further details of the product & allows the customer to add the product to the cart.
- The quantity can be amended, however currently each product only has 1 available of each so this is always set at 1 by default.

#### Cart 

- Displays the products the customer has added to the cart.
- The quantity can be amended, as previously mentioned though only 1 of each product is availble, due to the limited availabilty of the posters.
- Products can be removed from the cart.
- Links to the shipping form.
- If cart is empty the user is prompted to return to the store.

#### Checkout

- Two step process, firstly a page with the shipping details must be filled in. If the shipping details are by default taken from the customer's profile info.
- Secondly, the customer needs to fill in their payment details which are secured with the use of Stripe.
- Once payment has been approved the customer is presented with an order confirmation page, which displays the first product on the order along with the shipping address.

### Features Left To Implement

#### Shipping

- Once the site has gained popularity shipping cost will be calculated in the code.
- Domestic & International shipping options.
- Different classes of postage will allow users to pay for a premium service if required.

#### Featured Products

- Allow the shop to display new products in a featured products section, which would be shown on the home page.

#### News

- Have a news section which displays new products and info of upcoming releases.
- Allow customers to subscribe to newsletters via e-mail.

#### Languages

- Allow customers to change the language the site text is shown in.


#### FAQ Section

- Give further info about how the site works & provide contact details to get in touch with the site admin.

#### Story Reviews

- Allow users to leave comments & upvote & downvote stories.

#### Search Bar

- Allow users to search by category, author or keyword.
- Further functionality would be to filter results by popularity, most commented etc.

#### Further Languages

- Add a language choice option to cater to users from various countries.

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python
- Django

### Libraries

- Bootstrap
- JQuery & Popper
- FontAwesome
- Google Fonts

### Tools

- Github/Gitpod - Used to create & deploy website.
- AWS - Stores the media & provides Postgres database.
- Heroku - Used to deploy the application.
- Balsamiq 3 Mockups.
- Adobe Photoshop.
- Travis CI
- Google Chrome Dev Tools.

## Database

- The Postgres database was utilised with a fairly simple many-to-many database.
- Django was used to provide database models.
- The Database has two collections: Products & Categories.
- The category field in products links to a key id field for the relevant category in categories.

## Testing

- [Click Here For Testing File](https://github.com/JSudron/posterpocalypse-shop/blob/6aa23909641e2c10a7c184ec0f8fe6a422388df0/testing/testing.md)

## Deployment

### Cloning from GitHub

- Go to [Posterpocalypse](https://github.com/JSudron/posterpocalypse-shop) repository page.
- On the repository page click Clone or Download.
- In the Clone with HTTPs section, copy the clone URL for the repository.
- In your local IDE open Git Bash.
- Change the current working directory to the location where you want the cloned directory to be made.
- Type git clone, and then paste the URL you copied in Step 3 - `git clone https://github.com/JSudron/posterpocalypse-shop`.
- Press enter and your local clone will be created.

### Heroku Deployment

- Type `heroku ps:scale web=1` into bash terminal
- Create requirements.txt `sudo pip3 freeze --local > requirements.txt`.
- Create a Procfile `python app.py > Procfile`.
- Click on reveal Config Vars.
- Add each value from env.py file into the Config Vars.
- Go to deploy & choose GitHub as deployment method. 
- Choose the repository under App connected to GitHub.
- Go to Manual Deploys & click Deploy Branch.
- App is now deployed.

## Credits

### Content

- All written content was created by myself.

### Media

#### Images

- Product images taken from various sites, most predominantly Pinterest[https://www.pinterest.co.uk/].
- Logo & Jumbotron image created by myself in Adobe Photoshop.

#### Fonts

- Fonts from [Google Fonts](https://fonts.google.com/).

### Acknowledgements

#### Inspiration

- Parts of code were learnt from various sites, which was then amended by myself to obtain the look & feel I was after.
- Any code which was directly influenced from elsewhere is mentioned in comments above the code.
- [CodePen](https://codepen.io/) was used to get the features I required.
- [Awwwards](https://www.awwwards.com/) was used to look at a variety of sites for design inspiration.
- Colour scheme from [Coolors](https://coolors.co/).
- Slack & [Stack Overflow](https://www.stackoverflow.com/) were used to troubleshoot issues I had.
- Tutor Support was also invaluable, not only the support but their patience. Bunch of superstars!
- Also huge thanks to my mentor.

## Disclaimer

### This is for educational use only
