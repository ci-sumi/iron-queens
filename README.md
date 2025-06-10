# Iron Queens 🏋️‍♀️ 
Iron Queens is a B2C e-commerce platform empowering women in fitness by offering premium gym equipment, activewear, and wellness services. Catering to fitness enthusiasts, athletes, and beginners alike, the store provides high-quality workout gear alongside specialized services such as personalized yoga sessions, fitness coaching, and curated wellness programs.

Users can browse and purchase strength-training equipment, yoga mats, resistance bands, and stylish activewear designed for performance. Additionally, they can explore service offerings, book sessions, and read testimonials from a community of strong, like-minded women.

The website integrates Stripe for secure payments. Note: This is a demo site for educational purposes—please use test card details from Stripe’s documentation instead of real payment information.

Live Link: [Iron Queens](https://iron-queens-9a116e72c4d2.herokuapp.com/)

![Site Mockup] https://docs/readme_images/site_mockup.png


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
- As a shopper, I can view individual product details (description, price, sizes) so I can make informed decisions
- As a shopper, I can filter products by category (apparel/equipment/accessories) so I can narrow my search
- As a shopper, I can sort products by price, rating, or newness so I can find what suits me best
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
- As an admin, I can add/edit training programs so I can update offerings
- As an admin, I can manage customer inquiries so I can provide support

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
![Colour Palette](docs/readme_images/colour_scheme.png)
- **Primary Colours**:
  - `#D4AF37` (Gold) - Represents premium quality and achievement
  - `#2B2B2B` (Anthracite) - Creates strong contrast and modern elegance
- **Background Colours**:
  - `#F8F8F8` (Light Grey) - Provides clean product presentation
  - `#FFFFFF` (White) - Ensures maximum readability

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
  
![Home Page](docs/wireframes/home.png)  
*Featured sections: New arrivals, hero workout image, membership CTA*
</details>

<details>
<summary>👚 Workout Apparel Collection</summary>
  
![Workout Apparel](docs/wireframes/apparel.png)  
*Filterable grid of leggings, sports bras, and accessories with size guides*
</details>

<details>
<summary>💪 Training Programs</summary>
  
![Training Programs](docs/wireframes/training_programs.png)  
*Bookable sessions with coach bios and schedule*
</details>

### User Flow

<details>
<summary>🛍️ Gym Bag & Checkout</summary>
  
![Gym Bag](docs/wireframes/gym_bag.png)  
![Checkout](docs/wireframes/checkout.png)  
*Seamless flow with size validation and secure payment*
</details>

<details>
<summary>✅ Order Confirmation</summary>
  
![Order Confirmation](docs/wireframes/order_confirmation.png)  
*Includes delivery ETA and recommended matching items*
</details>

### Member Features

<details>
<summary>📊 Progress Dashboard</summary>
  
![User Profile](docs/wireframes/user_profile.png)  
*Tracks workout milestones with rewards system*
</details>

<details>
<summary>🏆 Success Stories</summary>
  
![Success Stories](docs/wireframes/success_stories.png)  
*Member transformations with product testimonials*
</details>

### Admin Portal

<details>
<summary>🛒 Product Management</summary>
  
![Product Management](docs/wireframes/product_management.png)  
*CRUD interface for inventory with size/color variants*
</details>

<details>
<summary>📅 Program Management</summary>
  
![Program Management](docs/wireframes/program_management.png)  
*Schedule builder for classes and personal training*
</details>


## Agile Methodology
Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com)


The 5 Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

## Database Schema 

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Heroku version. Below is an image of how the database models relate to each other:

![Database Schema](docs/readme_images/)

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

400 – Bad Request: IronQueens couldn’t process your request. Please try again.

403 – Forbidden: You don’t have permission to view this page. Try logging into the correct account.

404 – Page Not Found: The page you’re looking for may have moved or no longer exists.

500 – Server Error: A problem occurred on our end. We’re working to fix it promptly.