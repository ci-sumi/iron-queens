# Testing

- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [JSHINT](#jshint)
  * [Python Validation - Pycodestyle](#python-validation---pycodestyle)
  * [Lighthouse](#lighthouse)
- [Device Testing](#device-testing)
- [Browser Testing](#browser-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
  * [All Auth Pages](#all-auth-pages)
  * [Home Decor](#home-decor)
  * [Product Detail](#product-detail)
  * [Home Decor Management](#home-decor-management)
  * [Bag](#bag)
  * [Checkout](#checkout)
  * [Profile](#profile)
  * [Interior Design Services](#interior-design-services)
  * [Interior Design Management](#interior-design-management)
  * [Testimonials](#testimonials)
  * [Testimonial Management](#testimonial-management)
  * [Contact](#contact)
  * [Enquiries Dashboard](#enquiries-dashboard)
- [Fixed Bugs](#fixed-bugs)

## User Story Testing

### EPIC | Viewing and Navigation
*As a Site User, I can intuitively navigate around the site so that I can find content.*

- A navigation bar is visible on every page of the site which is fully responsive on different screen sizes.

![header](docs/readme_images/features/header.png)

*As a Site User, I can view a list of products so that I can select a product to view.*

- When the user navigates to the all products page they are presented with a list of all products from the database.

![all products](docs/readme_images/features/products_all.png)

*As a shopper, I can click on a product so that I can read the full product details.*
- When the user clicks on an individual product they are taken to the full product details.

![Product Detail](docs/readme_images/features/product_detail.png)

*As a shopper I can view a specific category of products so I can browse the type of products I'm looking for.*
- When clicking the 'Home Decor' link in the navbar the dropdown menu will show all the different categories. Clicking any of these will take the user to the products page, showing only items from the category selected. The category selected will display as the page heading.

![Categories](docs/readme_images/features/category.png)

![products](docs/readme_images/features/products.png)
 
*As a shopper I can search all products so that I can find what I am looking for*
- Located above the navbar is a search bar. On smaller screens, this bar becomes a search icon which when clicked will drop down the full bar. Any searched word will match itself to any text in the product's title, or description and display the results on the product's page.

![Search](docs/readme_images/features/search.png)

*As a shopper, I can sort all products so that I can view products based on price or title.*
- A sort box is located on the products page where users can sort all products by price in ascending or descending order and by title (A-Z). 


*As a site user, I can view  Services provided so I can understand what each service entails and make an enquiry if desired.*
- When the user navigates to the Interior Design Services page they are presented with a list of all  Services from the database along with detailed descriptions. An "Enquire Now" button displays beside each service which will take the user to the Contact form when clicked.

![Design Services](docs/readme_images/features/services.png)

*As a site user, I can read testimonials left by other customers so I see what feedback they gave on the Services they received.*
- When the user navigates to the Testimonials page they can see testimonials left by previous clients. 

![Testimonials](docs/readme_images/features/testimonials.png)

*As a site user, I can view pictures of previous interior design projects so that I can see if I like the results and build trust in the service provider.*


### EPIC | User Account and Profile
*As a site user I can register an account so that I can have a personal account.*
- A sign up button is located in the user options drop down menu in the Navbar. When the user clicks the button they are taken to the sign up page.

![Sign Up](docs/readme_images/features/signup.png)

*As a site user I can log in or log out of my account so that I can keep my account secure.*
- If the user has registered an account they can log in or log out by clicking the links in the user options drop down menu in the Navbar.

![Sign In](docs/readme_images/features/signin.png)
![Sign Out](docs/readme_images/features/signout.png)

*As a site user I can see my login status so that I know if I'm logged in or out.*

- Whenever a user logs in or logs out a toast message will appear notifying the user or their action.
- Their user name will display in the navbar.
- When signed in the options in the user menu will change to show Profile and Log Out buttons.

![Logged In](docs/readme_images/features/logged_in.png)

*As a site user I can save my personal details in my user profile so that I do not have to fill them out for future orders.*
- Users can fill in their personal details on their profile page. This information will be prepopulated for any future orders.
- When placing a new order, a checkbox under the delivery information can be checked to save the information just added.

![Delivery Details](docs/readme_images/features/delivery_info.png)

*As a site user I can view my order history so that I can remember what purchases I've made.*

- Once a user has created an account and placed an order, they can view the order history on their profile page.
- Clicking the order number will take you to a summary page of that order.

![Order History](docs/readme_images/features/order_history.png)

*As a site user I can recover my password in case I forget it so that I can recover access to my account.*
- On the sign-in page, a link to recover your password is located underneath the sign-in button. This uses the AllAuth functionality to reset the user's password. 

### EPIC | Purchasing
*As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.*

- Within the product detail page there is a quantity selector and an Add to Bag button. Shoppers can adjust the quantity by using the buttons located on either side of the input, or by typing in the amount.
- When the user clicks on the add to bag button, the chosen quantity of the product is added to the user's shopping bag.

![Product Detail](docs/readme_images/features/product_detail.png)

*As a shopper I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.

- As the user adds products to their bag, a toast message appears in the top right-hand corner of the screen informing the user that the item has been added, giving them a snapshot of the bag contents and the total cost of the bag.

![bag total](docs/readme_images/features/shopping_cart.png)

*As a shopper I can view the contents of my shopping bag at any time so I can see what is included and the total cost.*
- When the user clicks on the shopping bag icon in the nav bar they are taken to the shopping bag page which shows the products which the user has added to their cart, unit price, quantity and subtotal.
- The bottom of the page shows the bag total, delivery costs and then the grand total.

![shopping bag](docs/readme_images/features/shopping_total.png)

*As a shopper I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.*
- When the user is viewing the shopping bag, they are able to adjust the quantity of each product line item and update the subtotal by clicking the update icon.
- The user is able to delete the product by clicking the bin icon and the bag should be updated accordingly.

![Update Delete buttons](docs/readme_images/features/update_delete_buttons.png)

*As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.*
- On the Checkout page the user can see a summary of the line items within their order including a thumbnail image, the product name, the quantity, the unit cost and the overall total order cost on the right-hand side.

![checkout](docs/readme_images/features/check_out.png)

*As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.*
- When the user navigates to the checkout page, they can see the Stripe Elements UI where they can enter their card details securely and pay for their order.
- The user receives feedback if the card number is valid/invalid.

*As a shopper checkout as a guest so I don't have to sign up for an account.*
- Shoppers do not need an account to purchase any items. Regardless of whether a user is signed in, the checkout process remains the same.
-  When the user completes the checkout form and presses submit their order should be completed.

*As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.*
- When the user submits the checkout form, they are redirected to a Checkout Success page where they can see an order confirmation and a summary of their order.

![order_confirmation](docs/readme_images/features/order_confirmation.png)

*As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.*
- When the user has submitted their order they will receive a confirmation email to the email address they entered in their order form containing all the details of the order.

### EPIC | Admin & Store Management
*As a store owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.*
- When the site owner is logged in, a Home Decor Management option appears in the User drop-down menu.
- When the site owner navigates to the Home Decor Management page they can add a new product to the store through a user-friendly form. 

![add product](docs/readme_images/features/add_product.png)
- The site owner is able to edit and delete products by clicking buttons on both the main Home Decor page and also the product detail page.
- The edit form is pre-populated with the product information.

![edit product](docs/readme_images/features/edit_product.png)


*As a site owner, I can add/edit/delete interior design services provided through an easy-to-use interface so that I can manage the site's contents.*
- When the site owner is logged in, a Design Service Management option appears in the User drop-down menu.
- When the site owner navigates to the Design Service Management page they can add a new design service to the site through a user-friendly form. 

![Add Service](docs/readme_images/features/add_services.png)
- The site owner is able to edit and delete services by clicking buttons on the Interior Design Services page.
-  The edit forms fields are pre-populated with all service information. 

![edit Service](docs/readme_images/features/edit_service.png)


*As a site owner, I can add/delete images and location of previous design projects so that I can manage the site's contents.*
- When the site owner is logged in, a Previous Project Management option appears in the User drop-down menu.
- When the site owner navigates to the Previous Project Management page they can add details of a previous project to the site. through a user-friendly form. 


*As a site owner, I can view and delete customer enquiries on the front-end without having to access the admin panel.*
- When the site owner is logged in, an Enquiries Management option appears in the User drop-down menu.
- When the site owner navigates to the Enquiries Management page they can see a list of user enquiries sorted from newest to oldest.
- Emails that have been read are greyed out.

![Enquiries Dashboard](docs/readme_images/features/enquiry_dashboard.png)
- When the site owner clicks on an enquiry they are taken to the individual enquiry detail.
- The site owner can choose to delete the enquiry or to go back to the list of enquiries.



### EPIC | User Interaction
*As a site user, I can submit an enquiry form so that I can contact the site owner.*
- A user can open up the contact form by clicking on the "Enquire Now" button on the Interior Design Services page or by clicking the 'Contact' button in the Nav bar.
- The user can select the type of enquiry from a drop-down menu so that the site owner knows what the enquiry is about.
- If the user is logged in, their email address is prepopulated.
- When the form is submitted, the user receives an email confirmation of their enquiry so that they have a record of it.

![Enquiry Form](docs/readme_images/features/enquiry_form.png)

*As a site user, I can add / edit / delete a testimonial in relation to a consultation I received so that I can give my feedback.*
- When a logged-in user clicks on the "Add Testimonial" button on the Testimonials page, they can see a user-friendly form where they can add a new Testimonial to the site.

![Add Testimonial](docs/readme_images/features/)
- If the user is not logged in they are redirected to the log-in page.
- The user is able to edit and delete their own testimonials from buttons on the Testimonials Page.
- The edit forms fields are pre-populated with testimonial information.

![Edit Testimonial](docs/readme_images/features/edit_testimonial.png)

- The completed testimonial is automatically populated with the user's username and date underneath the body.

![Testimonials](docs/readme_images/features/testimonials.png)

*As a user, I can sign up for the website's newsletter so that I can keep up to date with new products and promotions*
- In the footer is a 'Newsletter' section. Here the user can input their email address to sign up.

![footer](docs/readme_images/features/footer.png)

## Validator Testing

HTML Validation
[The W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML.

These are the results of the validation:
*Home*
![Home](docs/readme_images/html_validation/home_html_validation.png)
*Products*
![Products](docs/readme_images/html_validation/products_html_validation.png)
*Products_Add*
![Products](docs/readme_images/html_validation/product_add__html_validation.png)
*Profile*
![Profile](docs/readme_images/html_validation/profile_html_validation.png)
*Orderhistory*
![Orderhistory](docs/readme_images/html_validation/order_history_html_validation.png)
*Contact*
![Contact](docs/readme_images/html_validation/contact_html_validation.png)
*Bag*
![Bag](docs/readme_images/html_validation/bag_html_validation.png)
*Testimonial*
![Testimonial](docs/readme_images/html_validation/testimonials_html_validation.png)
*Testimonial_Add*
![Testimonial_Add](docs/readme_images/html_validation/testimonials_add_html_validation.png)
*Services*
![Services](docs/readme_images/html_validation/services_html_validation.png)
*Services_Add*
![Services_Add](docs/readme_images/html_validation/services_add_html_validation.png)
*Signin*
![Signin](docs/readme_images/html_validation/signin_html_validation.png)

*Signup*
![Signup](docs/readme_images/html_validation/signup_html_validation.png)


CSS Validation
The [CSS Validation](https://jigsaw.w3.org/css-validator/) Service was used for CSS code.

These are the results of the validation:
*Home*
![Home](docs/readme_images/css_validation/base_css_validation.png)
*Index*
![Index](docs/readme_images/css_validation/index_css_validation.png)
*Checkout*
![Checkout](docs/readme_images/css_validation/checkout_css_validation.png)
*Product*
![Product](docs/readme_images/css_validation/product_css_validation.png)

![Services](docs/readme_images/css_validation/services_css_validation.png)
![Profile](docs/readme_images/css_validation/profile_css_html.png)

The [JSHint](https://jshint.com/) JavaScript Code Quality Tool was used to validate the sites JS code.
![Base](docs/readme_images/js_validation/base_js_validation.png)

![Country](docs/readme_images/js_validation/country_field_js_validation.png)

![Stripe](docs/readme_images/js_validation/stripe_js_validation.png)

Python Validation
For Python code, the [CI PEP8](https://pep8ci.herokuapp.com/) online validator was used to validate the code.
![Context](docs/readme_images/python/context.py.png)
![Profile](docs/readme_images/python/profile_view.py.png)
![Services](docs/readme_images/python/services.py.png)
![Services](docs/readme_images/python/services.py.pg)

## Lighthouse

Lighthouse validation was run on all pages in order to check accessibility and performance. Many warnings were fixed including 'Background and foreground colours do not have a sufficient contrast ratio' and the below scores were achieved.

Lighthouse Validation
The [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) tool was used to measure the performance of the website.

These are the results of the validation:
![Context](docs/readme_images/light_house/checkout.png)
![Context](docs/readme_images/light_house/contactus.png)
![Context](docs/readme_images/light_house/order_history.png)
![Context](docs/readme_images/light_house/product_management.png)
![Context](docs/readme_images/light_house/products.png)
![Context](docs/readme_images/light_house/profile.png)
![Context](docs/readme_images/light_house/services.png)
![Context](docs/readme_images/light_house/shopping_cart.png)
![Context](docs/readme_images/light_house/signin.png)
![Context](docs/readme_images/light_house/signout.png)
![Context](docs/readme_images/light_house/testimonial.png)


