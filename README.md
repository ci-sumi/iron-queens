# Iron Queens  
Iron Queens is a B2C e-commerce platform empowering women in fitness by offering premium gym equipment, activewear, and wellness services. Catering to fitness enthusiasts, athletes, and beginners alike, the store provides high-quality workout gear alongside specialized services such as personalized yoga sessions, fitness coaching, and curated wellness programs.

Users can browse and purchase strength-training equipment, yoga mats,stylish activewear designed for performance. Additionally, they can explore service offerings and read testimonials from a community of strong, like-minded women.

The website integrates Stripe for secure payments. Note: This is a demo site for educational purposes—please use test card details from Stripe’s documentation instead of real payment information.

Live Link: [Iron Queens](https://iron-queens-9a116e72c4d2.herokuapp.com/)

![Site Mockup](docs/readme_images/amiresponsive.png)


## Table of Contents

- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Imagery](#imagery)
    - [Fonts](#fonts)
    - [Wireframes](#wireframes)
- [Agile Methodology](#agile-methodology)
- [Database Schema](#database-schema)
- [Security Features](#security-features)
  - [User Authentication](#user-authentication)
  - [Form Validation](#form-validation)
  - [Database Security](#database-security)
  - [Custom Error Pages](#custom-error-pages)
- [Features](#features)
  - [Header](#header)
  - [Footer](#footer)
  - [Home Page](#home-page)
  - [User Account Pages](#user-account-pages)
  - [Profile](#profile)
  - [Fitness Products](#fitness-products)
  - [Product Detail](#product-detail)
  - [Product Management](#product-management)
  - [Shopping Bag](#shopping-bag)
  - [Checkout](#checkout)
  - [Wellness Services](#wellness-services)
  - [Services Management](#services-management)
  - [Success Stories](#success-stories)
  - [Testimonials](#testimonials)
  - [Contact Form](#contact-form)
  - [Enquiries Dashboard](#enquiries-dashboard)
  - [Error Pages](#error-pages)
- [Business Model](#business-model)
- [Marketing Strategy](#marketing-strategy)
  - [SEO](#seo)
  - [Content Marketing](#content-marketing)
  - [Social Media Marketing](#social-media-marketing)
  - [Email Marketing](#email-marketing)
- [Testing](#testing)
- [Deployment - Heroku](#deployment---heroku)
- [AWS Setup](#aws-setup)
- [Forking This Repository](#forking-this-repository)
- [Cloning This Repository](#cloning-this-repository)
- [Languages](#languages)
- [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## User Experience (UX)

Iron Queens Gym caters to fitness-focused women seeking high-quality workout apparel, gym equipment, and personalized training solutions designed specifically for women's needs.

### User Stories

#### EPIC | Product Browsing
- As a shopper, I can view all products at once so I can get an overview of what's available
- As a shopper, I can view individual product details (description, price) so I can make informed decisions
- As a shopper, I can filter products by category (apparel/equipment/accessories) so I can narrow my search
- As a shopper, I can sort products by price,names so I can find what suits me best
- As a shopper, I can search for specific items so I can find products quickly

#### EPIC | User Account
- As a user, I can register for an account so I can track my orders
- As a user, I can log in/out of my account so I can access my personal details
- As a user, I can recover my password so I can regain access if I forget it
- As a user, I can view my order history so I can track past purchases
- As a user, I can save my shipping details so I don't need to re-enter them

#### EPIC | Shopping & Checkout
- As a shopper, I can add items to my bag so I can purchase them later
- As a shopper, I can view my bag contents so I can review before purchasing
- As a shopper, I can adjust item quantities in my bag so I can modify my order
- As a shopper, I can enter payment details securely so I can complete my purchase
- As a shopper, I can receive order confirmation so I know my purchase was successful

#### EPIC | Admin & Management
- As an admin, I can add/edit/delete products so I can manage inventory
- As an admin, I can view customer orders so I can fulfill them
- As an admin, I can add/edit training  programs so I can update of services
- As an admin, I can manage testimonial so Ican update testimonials.

#### EPIC | Community Features
- As a user, I can read product reviews so I can make better choices
- As a user, I can contact support so I can get help when needed
- As a user, I can subscribe to newsletters so I can receive updates

### Future Features
The following features are planned for future implementation:
- Size recommendation tool based on body measurements
- Virtual try-on for apparel
- Integration with fitness tracking apps
- Loyalty rewards program

## Design

Iron Queens Gym combines athletic energy with luxurious sophistication through a refined design featuring gold accents and clean lines. The aesthetic celebrates women's strength while maintaining premium appeal.

### Colour Scheme
![Colour Palette](docs/readme_images/canva.png)
The palette maintains WCAG AA+ contrast standards while supporting the brand's luxurious identity.

### Imagery
**Hero Visual**:
- Features a powerful female athlete in mid-workout
- Gold lighting accents complement the colour scheme
- Captures movement and premium fabric details

**Product Imagery**:
- Studio-quality shots on neutral backgrounds
- Multiple angles showing technical features
- Detail close-ups of fabrics and stitching

**Supporting Visuals**:
- Before/after transformation shots
- Gym lifestyle images with gold accent elements

### Typography
**Primary Font**: 
- Raleway (600 SemiBold for headings, 400 Regular for body)
- Chosen for its geometric elegance and excellent legibility

**Fallback Stack**:
- Sans-serif system fonts (Arial, Helvetica, etc.)

### UI Elements
- Gold border accents on interactive elements
- Subtle shimmer effects on buttons
- Custom form styling with gold validation states
- Consistent card shadows for depth


/* Example gold accent styling */
.cta-button {
  background: transparent;
  border: 2px solid #D4AF37;
  color: #2B2B2B;
  transition: all 0.3s ease;
}

.cta-button:hover {
  background: rgba(212, 175, 55, 0.1);
}


### Wireframes

All wireframes were designed with mobile-first approach, focusing on the premium fitness experience for women.

### Key Pages

<details>
<summary>🏠 Home Page</summary>
  
![Home Page](docs/wireframes/home_page.png)  
*Featured sections: New arrivals, hero workout image 
</details>

<details>
<summary> Porduct Collection</summary>
  
![Workout Apparel](docs/wireframes/products_page.png)  
*Filterable gymequipments, gym wears, proteinbars and Gym Bottles
</details>

<details>
<summary>💪 Services</summary>
  
![Services](docs/wireframes/services_page.png)  
*Upcoming sessions of yoga,training*
</details>

### User Flow

<details>
<summary>🛍️ Gym Bag & Checkout</summary>
  
![Gym Bag](docs/wireframes/shopping_cart_page.png)  
![Checkout](docs/wireframes/checkout_page.png)  
*Seamless flow with size validation and secure payment*
</details>

<details>
<summary>✅ Order Confirmation</summary>
  
![Order Confirmation](docs/wireframes/order_summary.png)  
*Includes delivery ETA  and summary*
</details>

### Member Features

<details>
<summary>📊 Progress Dashboard</summary>
  
![User Profile](docs/wireframes/profile_page.png)  
*Tracks previous order of customer*
</details>

<details>
<summary>🏆 Success Stories</summary>
  
![Success Stories](docs/wireframes/testimonial_page.png)  
*Member transformations with product testimonials*
</details>

### Admin Portal

<details>
<summary>🛒 Product Management</summary>
  
![Product Management](docs/wireframes/product_management.png)  
*CRUD interface for inventory*
</details>

<details>
<summary>📅 Program Management</summary>
  
![Contactus](docs/wireframes/contactus_page.png)  
*Any one contact the site admin*
</details>


## Agile Methodology
Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/users/ci-sumi/projects/4)


The 5 Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

## Database Schema 

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Heroku version. Below is an image of how the database models relate to each other:

![Database Schema](docs/readme_images/database.png)

🔐 Security Features and Defensive Design

At IronQueens, the security of our users and the integrity of the platform are top priorities. Below are the core security measures and defensive design strategies integrated into the project:
🧍‍♀️ User Authentication and Authorization

Class-Based Views (CBVs):
    Utilized LoginRequiredMixin to restrict access to authenticated users only.
    Implemented UserPassesTestMixin to enforce object-level permissions, allowing users to edit or delete only their own content unless they are superusers.

Function-Based Views (FBVs):
Applied @login_required and @user_passes_test decorators to protect sensitive views and enforce role-based access.

📝 Form Validation

  All forms have server-side validation to prevent invalid or malicious data submission.

  Clear error messages inform users of the exact field that caused validation to fail.

  Input fields are sanitized and validated to defend against injection and formatting errors.

🗄️ Database Security

  Sensitive configuration variables like the database URL, Django secret key, and third-party API credentials (e.g., Stripe) are securely stored in env.py, keeping them out of source control.

  Parameterized queries and ORM-based database interaction prevent SQL injection vulnerabilities.

🛡️ CSRF Protection and Session Management

  All forms across the platform include Cross-Site Request Forgery (CSRF) tokens provided by Django.

  Secure session management practices are used, including secure cookie flags and session expiry settings to minimize session hijacking risk.

❌ Custom Error Pages

To improve user experience and clarity during error states, custom error pages were implemented:


404 – Page Not Found: The page you’re looking for may have moved or no longer exists.

## Features

### Header
![header](docs/readme_images/features/header.png)

**Logo**
- A customised logo was created using Hatchful by Canva which is a free logo generator.
- This logo is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user.

**Navigation Bar**

- The navigation bar is visible at the top of every page and includes links to the other pages.

**Search Bar**

![Search](docs/readme_images/features/search.png)
- The search bar displays above the nav bar.
- On smaller screens, this bar becomes a search icon which when clicked will drop down the full bar.
- Any searched word will match itself to any text in the product's title, or description and display the results on the product's page.


**User Icon**


- The User icon navigation link is a drop down menu which includes the Sign up and Log in links. 
- Once a user has signed in, their username will display beside the user icon.
- The options to Sign up or Log in will change to the option to log out once a user has logged in.
- Once a user has signed in, the 'My Profile' option becomes available in the User dropdown.

![Logged In](docs/readme_images/features/logged_in.png)

- If the superuser has signed in, more options such as 'Product Management', become available in the User dropdown.

![user menu](docs/readme_images/features/superuser_login.png)
- The navigation bar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small.
- Hovering over the links will turn the font gold.

**Bag Icon**

![bag](docs/readme_images/features/bag.png)
- Located on the right side of the navbar next to the User icon is the bag Icon.
- Once a product is added to the bag, a number displaying the total quantity of items appears, located at the top right of the bag icon.
- As the user adds products to their bag, a toast message appears in the top right-hand corner of the screen informing the user that the item has been added, giving them a snapshot of the bag contents and the total cost of the bag.

![bag total](docs/readme_images/features/add_bag_success.png)
- Clicking the bag icon navigates the user to the shopping bag page which displays a summary of what's been added.

### Footer

![footer](docs/readme_images/features/footer.png)

- The footer appears at the bottom of every page.
- The footer section includes links to Facebook, Instagram, Meta and Linkedin
- There is a newsletter signup section powered by Mailchimp where the user can input their email address to signup to the monthly newsletter.
- The Quick Links section has links to the main parts of the site including 'Contact Us'and 'Privacy Policy'.
- On the right hand side of the footer there are links high quality relevant websites including These links were included to increase the search rating of the website.
- Clicking all external links will open up the respective website in another tab to avoid pulling the user away from the site.

### Home Page

**Call to Action Section**

![Home page](docs/readme_images/features/call_action.png)

- The home page includes a call to action section which encourages the user to 'shop now' or to browse "design services" with the message "Style Your Space" and an image of stylish dining room.

**What We Do Section**

![What we do](docs/readme_images/features/what_we_do.png)

- The "What We Do' section gives a brief overview of what the site has to offer and includes relevant keywords in `<strong></strong>` tags to improve the site's search ranking.

### User Account Pages

**Sign Up**

![Sign Up](docs/readme_images/features/signup.png)

**Sign In**

![Sign In](docs/readme_images/features/signin.png)

**Log Out**

![Sign Out](docs/readme_images/features/signout.png)

- Django allauth was installed and used to create the Sign up, Log in and Log out functionality. 
- Success messages inform the user if they have logged in/ logged out successfully.
- When a user signs up for an account they must verify their email address by clicking on the authentication link emailed  to the address they provided.
- If a user forgets their password they can reset it by clicking the 'Forgot Password' on the log in page.


### Profile
**Delivery Details**

![Delivery Details](docs/readme_images/features/delivery_info.png)
- The delivery details section stores the user's delivery address and phone number.
- The information provided here is used to autofill the delivery address when placing an order.

**Order History**

![Order History](docs/readme_images/features/order_history.png)
- The order history section displays a list of every order the user has placed.
- The table displays the order number, date it was ordered and the order total.
- Clicking the order number will take the user to a summary page of that order.

### Gym (Products)

![all products](docs/readme_images/features/products_all.png)
- When clicking the  link in the navbar the dropdown menu will show all the different categories inclu'. 

![Categories](docs/readme_images/features/categories.png)
- The 'All' link will display a list of all products from the database.
- Clicking any of the categories will filter the products to only show products from the category selected.
- The category selected will display as the page heading.

![products](docs/readme_images/features/products.png)


- Each product card shows an image of the product, its title, excerpt and price.
- If the user is a superuser, edit and delete buttons will appear at the bottom of the product card.
- The products page is fully responsive, adjusting how many products are on each row depending on the user's screen size.
- A sort box is located onding the products page where users can sort all products by price in ascending or descending order and by title (A-Z).

![sort](docs/readme_images/features/product_sort.png)

### Product Detail

![Product Detail](docs/readme_images/features/product_detail.png)
- When the user clicks on an individual product card they are taken to the full product details. The link is a bootstrap stretched link so clicking anywhere on the card will work.
- The product detail page displays the product image, title, excerpt, price, product details and estimated dispatch time.
- If the user is a superuser, edit and delete buttons will appear below these details.

**Quantity Buttons**
- The quantity buttons are located underneath the product details and are used to add items to the bag.
- The plus and minus buttons increase and decrease the input value.
- If the value is set to 1 the minus quantity will be disabled. Respectively if the value is set to 99 the plus button is disabled.
- If the user manually types in a negative number or a number >99 and clicks "Add to Bag" an error button will appear informing the user of the parameters needed to be successful.
- Clicking the 'Add to Bag' button takes the number in the input field and adds that amount of products to the bag.
- Clicking the 'Keep Shopping' button takes the user back to the store.

### Home Decor Management
**Add Product**

![add product](docs/readme_images/features/add_product.png)
- The add product page can be accessed by clicking the 'Add Product' button on the Home Decor page or in the user dropdown menu, under Home Decor Management. These options are only visible to superusers.
- If a user tries to add a product (by changing the url) without being a superuser they are redirected to a custom 404 page
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- The SKU field must be unique. An error message will appear if the SKU already exists.
- If a price is added with more than 6 digits the form will fail and an error message will appear under the price field.
- The user can upload a photo if they wish. If they choose not to, a default image displays as their product image.
- Clicking the 'Add Product' button at the bottom of the form will create the product providing there are no errors on the form.
-  The user will receive a success message notifying them that the product has been successfully added.

**Edit Product**

![edit product](docs/readme_images/features/edit_product.png)
- The superuser can choose to edit a Product by clicking the edit button on the product card or on the product detail page. 
- The form opens with all fields populated with the original content.
- The image field displays a thumbnail of the existing image and has a checkbox option to remove it. Checking this will change the image to the default image.
- If a user tries to add a product (by changing the url) without being a superuser they are redirected to a custom 403 page.
- The superuser will receive a success message notifying them that the product has been successfully updated.

**Delete Product**


- The superuser can choose to delete a Product by clicking the delete button on the product card or on the product detail page. 

- The superuser will receive a success message notifying them that the product has been successfully deleted.

### Bag

![shopping bag](docs/readme_images/features/shopping_cart.png)
- When the user clicks on the shopping bag icon in the nav bar they are taken to the shopping bag page which shows the products which the user has added to their cart, unit price, quantity and subtotal.

**Quantity Buttons**
- The quantity input box displays the product quantity the user has added to their bag.
- The plus and minus buttons increase and decrease the input value.
- If the value is set to 1 the minus quantity will be disabled. Respectively if the value is set to 99 the plus button is disabled.

**Update and Delete Buttons**

![Update Delete buttons](docs/readme_images/features/update_delete_buttons.png)
- Clicking the 'update' icon button saves any changes to the quantity and updates the item's subtotal.
- Clicking the 'Bin' icon button removes the item completely from the user's bag.
- If the user manually types in a negative number and clicks 'update', the item will be removed from the item from the bag.?
- If the user manually types in a number >99 and clicks 'update' an error message will display informing the user of the correct parameters.

**Total Section**
- At the end of the line items is a summary of the costs.
- The summary features the bags total, delivery cost and the grand total to pay.
- Underneath the grand total users will find a message informing them of how much more they need to spend to receive free delivery if they haven't already met the free delivery threshold (€250). ?
- Beneath the grand total is two buttons. From here the user can either continue to the checkout or return to the products page by clicking 'Continue Shopping'.

### Checkout 

![checkout](docs/readme_images/features/check_out.png)

**Details**
- Within the details section the user can fill out their contact details, delivery address, and card number.
- If the user is a guest, a link to create an account or login will be present.
- If the user is signed in a checkbox to save the delivery information can be checked.
- If the user is signed in and has delivery information saved, the delivery details and email address will be automatically filled in.
- If a user leaves a required field empty, inputs whitespace in a required field or includes text in the phone number field an error message will prompt the user to 'Fill in the field' or 'match the format requested'

**Order Summary**
- The order summary section details all the items about to be purchased, along with the quantity, subtotal and a grand total.
- Next to the order summary title will be a number reflecting the total number of items that appear in the order.
- Clicking the product image in the summary will take the user to that product's detail page.

**Payment**
- The card payment is handled by Stripe to ensure secure payment.
- Incorrect card numbers will automatically show an invalid card number error.
- A loading screen will appear when a payment is being processed to stop the user clicking away.
- There is a warning message at the bottom of the page informing the user of how much their card is about to be charged.
- If the payment form doesn't submit properly or the user closes the browser during the wait animation, the order will still be created in the database through the webhook. 
- Once the payment is processed, the webhook will search the database to confirm the order exists. If it cannot find it, it will create one using the payment information.

**Confirmation**

![order_confirmation](docs/readme_images/features/order_confirmation.png)
- Once the order has been processed the user is taken to the checkout success page.
This page summarises the completed order.
- An email will be sent to the user with their order confirmation
- At the end of the summary is a 'Keep Shopping' button that takes the user back to the Home Decor page.

### Services

![Services](docs/readme_images/features/services.png)
- The Interior Design Services page can be accessed by clicking on the link in the nav bar. 
- When the user navigates to the Interior Design Services page they are presented with a list of all Interior Design Services from the database including image, title and detailed description. 
- An "Enquire Now" button displays beside each service which will take the user to the Contact form when clicked.
- If the user is a superuser, edit and delete buttons will display below each services' details instead of the enquire now button.

### Design Services Management
**Add Service**

![Add Service](docs/readme_images/features/add_services.png)
- The add service page can be accessed by clicking the 'Add Service' button on the Interior Design Services page or in the user dropdown menu, under Design Services Management. These options are only visible to superusers.
- If a user tries to add a service (by changing the url) without being a superuser they are redirected to a custom 403 page.
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- The user can upload a photo if they wish. If they choose not to, a default image displays as their service image.
- Clicking the 'Add Service' button at the bottom of the form will create the service providing there are no errors on the form.
-  The user will receive a success message notifying them that the service has been successfully added.???

**Edit Service**

![edit Service](docs/readme_images/features/edit_service.png)
- The superuser can choose to edit a Service by clicking the edit button under the service description on the Interior Design Services Page. 
- The form opens with all fields populated with the original content.
- The image field displays a thumbnail of the existing image and has a checkbox option to remove it. Checking this will change the image to the default image.
- If a user tries to add a service (by changing the url) without being a superuser they are redirected to a custom 403 page.
- The superuser will receive a success message notifying them that the service has been successfully updated.

**Delete Service**

- The superuser can choose to delete a Service by clicking the delete button under the service description on the Interior Design Services Page.

- The superuser will receive a success message notifying them that the service has been successfully deleted.


### Testimonials

![Testimonials](docs/readme_images/features/testimonials.png)
- The testimonials page can be accessed by clicking the link in the nav bar.
- When the user navigates to the Testimonials page they can see all testimonials left by previous clients. 
- Each testimonial displays the Design Service they relate to, the date and the user's name.

**Add Testimonial**

![Add Testimonial](docs/readme_images/features/testimonials.png)
- When a logged-in user clicks on the "Add Testimonial" button on the Testimonials page, they can see a user-friendly form where they can add a new Testimonial to the site.
- If the user is not logged in they are redirected to the log-in page.
- The completed testimonial is automatically populated with the user's username and date underneath the body.

**Edit Testimonial**

![Edit Testimonial](docs/readme_images/features/testimonials.png)
- The user is able to edit their own testimonials by clicking the edit button which display beside their own testimonial on the Testimonials Page.
- The edit form fields are pre-populated with the existing testimonial text.
- If a user tries to update a testimonial (by changing the url) without being signed in they are redirected to the log in page.
- If a user tries to update another user's testimonial (by changing the url) they receive a custom 403 error.
- The superuser can edit anyone's testimonial.
- The user will receive a success message notifying them that the testimonial has been successfully updated.

**Delete Testimonial**

![Delete Testimonial](docs/readme_images/features/testimonials.png)
- The user can choose to delete their own testimonial by clicking the delete button which display beside their own testimonial on the Testimonials Page.
- The user is asked to confirm if they wish to delete the testimonial or cancel.
- The user will receive a success message notifying them that the testimonial has been successfully deleted.
- If a user tries to delete a testimonial (by changing the url) without being signed in they are redirected to the log in page.
- If a user tries to delete another user's testimonial (by changing the url) they receive a custom 404 error.
- The superuser can delete anyone's testimonial.

### Contact Form

![Contact Form](docs/readme_images/features/contactus.png)
- A user can open up the contact form by clicking on the "Contactus" button on the Interior Design Services page or by clicking the 'Contact' button in the Nav bar.
 
- The form contains a drop down menu where the user can select the type of enquiry from a list so that the site owner knows what the enquiry is about.
- The user must fill out all the fields that have an Asterix. If the form is submitted with any of these fields left blank or with just whitespace then an error message will appear above that particular field, notifying the user of the issue.
- When the form is submitted, the user shows the message  confirmation of their enquiry.

### Error Pages
Custom Error Pages were created to give the user more information on the error and to guide them back to the site.

![404 error](docs/readme_images/features/404_error_page.png)


## Business Model

Fresh Nest's Business Model is Business to Consumer (B2C). Products and services are sold directly from Ironqueens to consumers who are the end-users. 
A customer of IronQueens would be someone who is most likely an adult who is interested in buying Gym equipments and wears.

## Marketing Strategy

A number of different marketing strategies have been utilised to promote IronQueens including SEO, content marketing, social media marketing and email marketing. Each of these strategies have been discussed individually below:  

### SEO
Several SEO techniques were undertaken in order to ensure the site ranks highly in search engine results:

**Keywords:** 

A mixture of short tail and long tail keywords were carefully considered for the site. Keyword research was performed by checking Google search results, looking at competitor's keywords and by utilising wordtracker.com. 

An initial list of topics and keywords generated can be seen below. This list was then refined based on relevance and authority.

The most relevant keywords have been added to the site's meta-keywords and meta-description. These keywords have also been carefully included in page titles, headings, site content, `<strong></strong>` tags, image alt attributes and anchor tag links across the site. 
🏋️‍♀️ Core Product Keywords

    women’s gym equipment

    premium gym gear for women

    activewear for women

    fitness apparel for women

    strength training equipment women

    yoga mats women

📈 Wellness & Services Keywords

    women's wellness programs

    female-focused fitness coaching

    personalized yoga sessions women

    workout coaching for women

💳 Platform & Trust Keywords

    secure Stripe payments

    demo e‑commerce fitness site

    test payments gym equipment

🎯 Brand & Niche Keywords

    Iron Queens fitness store

    Iron Queens workout apparel

    female fitness equipment online

🛠️ Technical / SEO Keywords

    Django fitness store

    Python gym store

    AWS S3 e‑commerce platform

    Postgres gym database

    Bootstrap fitness site

    mobile-first gym website

🧩 Long-Tail Keywords (for deeper reach)

    buy yoga mats designed for women

    best resistance bands for female athletes

    women’s strength training equipment online

    female wellness coaching booking platform



**External Links:**

Included in the site footer are links to other high quality relevant websites including Houzz, Institute of Designers Ireland, and The Interiors Association. These links show search engines that the page is of good quality improving the site's ranking further. 

**Building Trust:**

In order to build brand trust, a testimonial page for interior design services has been included in the site with a link to the page being included in the page footer as well as the main nav bar. 

The page footer also includes links to the privacy policy to inform users about how their data is being collected and processed.

**Sitemap and robots.txt**

A sitemap file with a list of important page URLs was created to ensure that search engines are able to understand the site's structure and easily navigate through the site. This was made using xml-sitemaps.com.

A robots.txt file was created to tell search engines where they are not allowed to go on the website. This improves SEO by increasing the quality of the site

### Content marketing 
The site showcases high quality images of previous interior design projects projects in order to attract potential new clients. The photos allow the business to show off their expertise and style and build up trust with the customer.

### Social Media Marketing 
For this site, a Facebook business page has been created for organic social media marketing. The Facebook page includes a 'Shop Now' button which takes the user to the Fresh Nest website. The page pairs well with the content media marketing on the main site as images of previous projects and new product arrivals can be shared easily.
Facebook now prioritizes Facebook Shops (hosted by Meta), especially in the New Pages Experience. That’s why you're only seeing:

    “Shop on Facebook”

    “Connect another tool” (e.g. Shopify, BigCommerce, etc.)

Unfortunately, they’ve removed the ability to link external stores directly from the “Shop Now” button in some regions and accounts.
## 📲 Facebook Page Integration

To link the live store to your Facebook Business Page:

1. Facebook currently does **not support external links** with the **“Shop Now”** button directly.
2. Instead, use the **“Learn More”** button as a workaround:
   - Go to your Facebook Business Page.
   - Click the **Edit Action Button** below your cover photo.
   - Select **“Learn More”**.
   - Choose **“Link to Website”** and enter:  
     `https://iron-queens-9a116e72c4d2.herokuapp.com/`
3. Save and test the button — it will redirect users to the live Iron Queens store.

![learnmore](docs/readme_images/features/learn_more.png)
![learnmore](docs/readme_images/features/action_facebook.png)


![Facebook Page](docs/readme_images/features/facebook.png)

### Email Marketing
Visitors to the site can sign up to the newsletter and do not need to have an account to do so. A signup box is included in the footer of the site. This allows the business to share news with customers and potential customers including new products/services and special offers. Mailchimp was used to create this service. 

## Testing
Testing and results can be found [here](/TESTING.md)

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.
- Go back to your IDE and install 2 more requirements:
    - `pip3 install dj_databse_url`
    - `pip3 install psycopg2-binary` 
- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- In settings.py file import dj_database_url, comment out the default configurations within database settings and add the following: 

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
- Run migrations and create a superuser for the new database. 
- Create an if statement in settings.py to run the postgres database when using the app on heroku or sqlite if not

```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    }
```

- Create requirements.txt file by typing `pip3 freeze --local > requirements.txt`
- Create a file named "Procfile" in the main directory and add the following: `web: gunicorn project-name.wsgi:application`
- Add Heroku to the ALLOWED_HOSTS list in settings.py in the format ['app_name.heroku.com', 'localhost']

- Push these changes to Github.

### Update Heroku Config Vars
Add the following Config Vars in Heroku:

|     Variable name     |                           Value/where to find value                           |
|:---------------------:|:-----------------------------------------------------------------------------:|
| AWS_ACCESS_KEY_ID     | AWS CSV file(instructions below)                                               |
| AWS_SECRET_ACCESS_KEY | AWS CSV file(instructions below)                                               |
| DATABASE_URL          | Postgres generated (as per step above)                                        |
| EMAIL_HOST_PASS       | Password from email client                                                    |
| EMAIL_HOST_USER       | Site's email address                                                          |
| SECRET_KEY            | Random key generated as above                                                 |
| STRIPE_PUBLIC_KEY     | Stripe Dashboard > Developers tab > API Keys > Publishable key                |
| STRIPE_SECRET_KEY     | Stripe Dashboard > Developers tab > API Keys > Secret key                     |
| STRIPE_WH_SECRET      | Stripe Dashboard > Developers tab > Webhooks > site endpoint > Signing secret |
| USE_AWS               | True (when AWS set up - instructions below)                                   |

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.


## AWS Set Up
### AWS S3 Bucket
- Create an AWS account.
- From the 'Services' tab on the AWS Management Console, search 'S3' and select it.
- Click 'Create a new bucket', give it a name(match your Heroku app name if possible), and choose the region closest to you.
- Under 'Object Ownership' select 'ACLs enabled' and leave the Object Ownership as Bucket owner preferred.
- Uncheck block all public access and acknowledge that the bucket will be public.
- Click 'Create bucket'.
- Open the created bucket, go to the 'Properties' tab. Scroll to the bottom and under 'Static website hosting' click 'edit' and change the Static website hosting option to 'enabled'. Copy the default values for the index and error documents and click 'save changes'.
- Open the 'Permissions' tab, locate the CORS configuration section and add the following code:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- In the 'Bucket Policy' section and select 'Policy Generator'.
- Choose 'S3 Bucket Policy' from the type dropdown.
- In 'Step 2: Add Statements', add the following settings:
    - Effect: Allow
    - Principal: *
    - Actions: GetObject
    - ARN: Bucket ARN (copy from S3 Bucket page)
- Click 'Add Statement'.
- Click 'Generate Policy'.
- Copy the policy from the popup that appears
- Paste the generated policy into the Permissions > Bucket Policy area.
- Add '/*' at the end of the 'Resource' key, and save.
- Go to the 'Access Control List' section click edit and enable List for Everyone (public access) and accept the warning box.


### IAM
- From the 'Services' menu, search IAM and select it.
- Once on the IAM page, click 'User Groups' from the side bar, then click 'Create group'. Choose a name and click 'Create'.
- Go to 'Policies', click 'Create New Policy'. Go to the 'JSON' tab and click 'Import Managed Policy'. 
- Search 'S3' and select 'AmazonS3FullAccess'. Click 'Import'.
- Get the bucket ARN from 'S3 Permissions' as per above.
- Delete the '*' from the 'Resource' key and add the following code into the area:

```
"Resource": [
    "YOUR-ARN-NO-HERE",
    "YOUR-ARN-NO-HERE/*"
]
```

- Click 'Next Tags' > 'Next Review' and then provide a name and description and click 'Create Policy'.
- Click'User Groups' and open the created group. Go to the 'Permissions' tab and click 'Add Permissions' and then 'Attach Policies'.
- Search for the policy you created and click 'Add Permissions'.
- You need to create a user to put in the group. Select users from the sidebar and click 'Add user'.
- Give your user a user name, check 'Programmatic Access'.
- Click 'Next' and select the group you created.
- Keep clicking 'Next' until you reach the 'Create user' button and click that.
- Download the CSV file which contains the AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID needed in the Heroku variables as per above list and also in your env.py.


### Connecting S3 to Django 
- Go back to your IDE and install 2 more requirements:
    - `pip3 install boto3`
    - `pip3 install django-storages` 
- Update your requirements.txt file by typing `pip3 freeze --local > requirements.txt` and add storages to your installed apps.
- Create an if statement in settings.py 

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-your-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

```
- Then add the line 

    - `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell django where our static files will be coming from in production.


- Create a file called custom storages and import both our settings from django.con as well as the s3boto3 storage class from django storages. 
- Create the following classes:

```
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

- In settings.py add the following inside the if statement:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

- and then add the following at the top of the if statement:
```
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

- Go to S3, go to your bucket and click 'Create folder'. Name the folder 'media' and click 'Save'.
- Inside the folder, click 'Upload', 'Add files', and then select all the images that you are using for your site.
- Then under 'Permissions' select the option 'Grant public-read access' and click upload.
- Your static files and media files should be automatically linked from django to your S3 bucket.

## Forking this repository
- Locate the repository at this link [Fresh Nest](https://github.com/ci-sumi/iron-queens).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

## Cloning this repository
To clone this repository follow the below steps: 

1. Locate the repository at this link [Fresh Nest](https://github.com/ci-sumi/iron-queens). 
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

## Languages

- Python
- HTML5
- CSS3
- Javascript

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [JQuery](https://jquery.com/)
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [SQLite](https://www.sqlite.org/index.html) - was used as the database during production.
- [Stripe](https://stripe.com/ie) used for the payments system.
- [AWS](https://aws.amazon.com/?nc2=h_lg) used for file storage.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Responsinator](http://www.responsinator.com/) - Used to verify responsiveness of website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Grammerly](https://app.grammarly.com/) - used to proof read the README.md
- [Techsini](https://techsini.com/multi-mockup/index.php) - Site mockup generator
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling
- [Hatchful](https://hatchful.shopify.com/): Used to generate custom logo
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown
- [Sitemap Generator](www.xml-sitemaps.com): used to create sitemap.xml 
- Shopify  Used to create the site's privacy policy
- [Mailchimp](https://mailchimp.com/?currency=EUR): Used to create the newsletter signup functionality.


## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Pexels](https://www.pexels.com/): Imagery on the site was sourced from Pexels.com
- [Unsplashed](https://unsplash.com/): Imagery on the site was sourced from Unsplash
- [Code Institute - Boutique Ado Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)
- [Stack Overflow](https://stackoverflow.com/questions/19619428/html5-form-validation-pattern-alphanumeric-with-spaces): To prevent form being submitted with whitespace


## Acknowledgments

Many thanks to my mentor 
Tomislav for his support and advice. Thanks to The Code Institute slack community for their quick responses and very helpful feedback.