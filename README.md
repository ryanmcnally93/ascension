# Ascension

<img src="/media/readme-images/main-image-ascension.webp" width="100%" alt="Ascension, on multiple devices" style="display: inherit; ">

This is a Django web application for Ascension, a music studio based in Birmingham. Languages used include HTML, CSS, JavaScript and Python, created using Django Crispy Forms, All Auth, Stripe, Pillow & Bootstrap.

This project allows users to book studio time with engineers or rehearsal rooms for practicing musicians/bands. It also has a small shop which is situated in the foyer, where musicians can buy strings, capos, and other small instrument parts.

The web application allows the creator to create more listings in the products section, and more studios, sound engineers and rehearsal rooms.

<p align="center">

<img src="https://img.shields.io/github/stars/ryanmcnally93/ascension?style=social" style="max-width: 100%; margin: 0 10px 10px 0;" alt="Stars">

<img src="https://img.shields.io/github/repo-size/ryanmcnally93/ascension" style="max-width: 100%; height: 20px; margin: 0 0 10px 10px;" alt="Size of repo">

<br>

<img src="https://img.shields.io/github/issues-raw/ryanmcnally93/ascension" style="max-width: 100%; height: 20px margin-right: 10px;" alt="Open issues">

<img src="https://img.shields.io/github/last-commit/ryanmcnally93/ascension?color=green&style=for-the-badge" style="max-width: 100%; height: 20px; margin-left: 10px;" alt="GitHub last commit">

</p>

## Contents

- [Deployment](#deployment)
- [UX](#ux)
  * [Project Goals](#project-goal)
  * [User Stories](#user-stories)
  * [Model Schema](#model-schema)
  * [Design Choices](#design-choices)
  * [Wireframes](#wireframes)
  * [Prototype](#prototype)
  * [App Setup](#app-setup)
  * [Q and A of Potential Users](#q-and-a-of-potential-users)
  * [Competitor Review](#competitor-review)
  * [Roadmap](#roadmap)
  * [Existing Features](#existing-features)
  * [Features Left to Implement](#features-left-to-implement)
- [Testing](#testing)
  * [Fixed Bugs](#fixed-bugs)
  * [Unfixed Bugs](#unfixed-bugs)
  * [Responsive Design](#responsive-design)
- [Credits](#credits)
  * [Code](#code)
  * [Web Tools](#web-tools)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## Deployment

To deploy my Heroku project, I followed the steps set by Code Institute.

- Create an account on Heroku
- Create an account on ElephantSQL
- Create new instance and copy database URL
- Create a Procfile and requirements.txt file
- Setup hosting for static and media files with Amazon Web Services - S3 (Simple Storage Service)
- Create AWS Groups, Policies and Users
- Enter config vars, including the copied URL, Stripe payment variables, and email variables.
- Setup email if statement in settings.py that sends emails to me
- Click on deploy, connect to github, find the repository
- Click Deploy Branch
- Once that is done, click more, and run console.

An issue I had when the site was deployed was removing the correct forward slashes from the URL's of images and links, but this has since been resolved.

## UX

### Project Goal

To allow users to book sessions in either the studio and/or the rehearsal rooms, whilst also giving them the option to order small parts from a small online store.

#### Business and Developer Goals

As the business owner I want users to believe in both our studio's and engineer's capabilities. I want the site to look "record label level" professional. I want users to be able to easily navigate through the three main site pages and be drawn in by the use of imagery and ease of use. I want them to be able to purchase or hire easily, and for bookings and stock to change when this happens.

I also need to be able to add, change and delete items myself.

- To create a site that has user authentication.
- To create a site that updates when products are bought/hired.
- To promote a professional looking studio and capable engineers.
- To have a site with complete ease of use.
- To have complete CRUD functionality over the products I am offering.

| Goals                                                        | How are they achieved? |
| :----------------------------------------------------------- | :--------------------- |
| Site that has user authentication.                           | Using all auth templates and creating session cookies. |
| Site that updates when products are bought/hired.            | Add to card buttons and quantity buttons add and subtract from cart cookie. |
| Promote professional looking studios and engineers.          | Sharp edges, blues and dark silvers used, looks slick. |
| Site with complete ease of use.                              | Every page has a choice of navbar options, back forward and back buttons. |
| Complete CRUD functionality over the products I am offering. | Administrator can add, edit and delete products. User can add edit and delete cart products. |

#### Recording Musician Goals

As a professional recording musician, I want to know that the engineer is friendly, easy going, and has a vast amount of knowledge and experience. I want the studio to be professional and clean, with high quality equipment. I want the site to invoke confidence of these expectations being met.

- Information on experienced engineers.
- Images of the studio and it's equipment.
- Proof of achievements on other songs.
- Ease of use with booking.

| Goals                                    | How are they achieved? |
| :--------------------------------------- | :--------------------- |
| Information on experienced engineers.    | Information on meet the engineers page |
| Images of the studio and it's equipment. | This information is on the rehearsals homepage, and there are links available in the product information pages. |
| Proof of achievements on other songs.    | Artists we've worked with section is available on the record studio homepage. |
| Ease of use with booking.                | Clicking a date gives time options, clicking that and adding to cart creates a cart object with the relevant date and time. |

#### Band Member Goals

As a band member I want to know what equipment is in the rehearsal room I'm hiring. I want images to show a clean, tidy room with decent equipment. I want the booking system to be easy to navigate through.

- Information on equipment provided in each room.
- Images of equipment and room.
- Ease of use with booking.

| Goals                                           | How are they achieved? |
| :---------------------------------------------- | :--------------------- |
| Information on equipment provided in each room. | This is with the rehearsals page. |
| Images of equipment and room.                   | Within products, product information and rehearsals. |
| Ease of use with booking.                       | Click date, time and add to cart. |

#### Sound Engineer Goals

As a soung engineer, I want my achievements to be there for users to see. I want my details to be friendly, welcoming and professional. I want my best equipment to be on show so musicians know they are getting value for money and high quality of service. I also want them to know me by name and face so they can spread the word about me as an engineer.

- Detailed section about me including image.
- Information on my achievements.
- Images of my studio.

| Goals                                      | How are they achieved? |
| :----------------------------------------- | :--------------------- |
| Detailed section about me including image. | All on the meet the engineers page. |
| Information on my achievements.            | Meet the engineers offers some insight, maybe this can be built on in a future section. |
| Images of my studio.                       | Within the product and product information. |

### User Stories

#### Unregistered User

- Should be able to view products and pages as normal.
- User-options should be 'login' or 'register' only.
- Should be able to add to cart as normal.
- Typing url for disallowed pages should take user to the login page.
- Checkout page requires URL to assure unregistered user cannot make purchases.

#### Logged in User

- Should extend all the same privileges as the unregistered user.
- Should still not allow you to access the Add and Edit product pages.
- Should be able to checkout using test card data.
- Should be able to access Profile page, with order history.
- Should be able to save billing info.

#### Administrator

- Should extend all the same privileges as the logged in user.
- Should have access to add and edit products pages.
- Should be able to edit and delete products on products page and product information pages.
- Should be able to delete products.

### Model Schema

Here is a diagram that explains the relationships between each model.

<img src="/media/ascension-schema.png" width="80%" alt="The fonts used" style="display: inherit; ">

### Design Choices

The website needs to look professional and high tech, we want customers to feel like this is a high end studio that knows their craft. We want thea dark blue environment associated with being in a studio, I'm going for electric blue to stay relative, with sharp edges.

#### Fonts

- I decided to use the 'Raleway' font as it has character in lowercase but has a very professional look in uppercase. This has been used across the whole web-application.

<img src="/media/readme-images/fonts.webp" width="50%" alt="The fonts used" style="display: inherit; ">

#### Icons

- The user icon is used within the navbar for the user options, from logging in to viewing your profile.
- The cart has a shopping-cart icon, as does the back to cart button on the checkout page.
- The social media icon are within the footer, with the same styling as the rest of the site.
- Secure payment and complete order have the safety lock icon. So users know this is secure.
- The toast messages have relevant ticks, x's, and warning and information icons.

<img src="/media/readme-images/icons-1.webp" width="50%" alt="Navbar Icons" style="display: inherit; ">

<img src="/media/readme-images/icons-2.webp" width="50%" alt="Footer Icons" style="display: inherit; ">

#### Colours

- I wanted to use an electric blue initially, to give the page a more digital look. I settled in the end for a dark turquoise.
- The main colours are #282C2E, a dark grey colour, and #033A54 the dark turquoise.
- The navbar is turquoise and the footer grey, with the mobile navbar also being grey.
- The primary buttons are turquoise and the secondary buttons are grey, the hover qualities change the buttons main colors with white and the white test to the main color. This is the same throughout.

<img src="/media/readme-images/colours.webp" width="50%" alt="Primary and Secondary coloured buttons" style="display: inherit; ">

#### Styling

- Feel of the site is electric blue, sharp edges and sparky feel to it.

<img src="/media/readme-images/styling.webp" width="50%" alt="Styling used" style="display: inherit; ">

#### Backgrounds & Images

- The background images have hints to what the page is about, as well as being musically themed.
- The cover image is that of a studio in use.
- The record homepage is another studio shot.
- The rehearsals homepage is an image of someone enjoying a major performance.
- The checkout success is someone using a loop pedal, this represents another successful purchase.
- The sign in page is the first thing a vocalist sees when they enter the room, headphones rested on a microphone.
- The register button is someone about to start a long journey.
- And the log out button is guitar that has been put away, resting on its stand.
- The product images are all relevant to what they are advertising.

<img src="/media/readme-images/backgrounds.webp" width="70%" alt="Example of a background used" style="display: inherit; ">

### Wireframes

I created these wireframes using [Balsamiq Wireframes](https://balsamiq.com/wireframes/).

<img src="/media/readme-images/index-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/record-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/rehearse-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/shop-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/about-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/engineer-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/login-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">
<img src="/media/readme-images/products-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/product-info-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/manage-items-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/profile-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/bag-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/checkout-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

<img src="/media/readme-images/successful-checkout-wireframe.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

### Prototype

This prototype of the index page was made using [Figma.com](https://www.figma.com).

<img src="/media/readme-images/prototype-index.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

### App Setup

Originally, I wanted to have the products within their allocated app (Rehearse, Record and Shop), I was thinking of having the products html's display in different colours when accessed through these different apps. I later decided against this as the colours would not go well with the rest of the sites design and having all the products accessible through one app is so much simpler and easier.

This means that like the home app: the record, rehearse and shop apps serve as homes for their respective templates only. With the record app containing 'Meet the Engineers' too.

The products page can detect whether the user has arrived at the page through one of the apps, and displays the page differently with either a gold or lightblue border and specific page title.

### Q and A of Potential Users

I've asked the following questions to:

- A band member friend (drummer).
- A solo musician.
- And a sound engineer.

#### Q1 - What did you make of the products on offer? Where there any items you'd expect that weren't there?

Drummer: 

- "Considering the shop size there is a lot on offer."

Solo Artist: 

- "Products seem geared towards guitar players and drummers who I assume would be the biggest users of a music studio. I did wonder about Reeds for woodwind instruments but suppose you wouldn't get much call for them. Was surprised to see a box of pens for sale?"

Engineer: 

- "I liked the products on offer and felt there was a good range of items. I couldn’t think of any items I would need which weren’t on offer"

#### Q2 - What makes a great shopping experience?

Drummer:

- "Being able to move from page to page smoothly and easily, and good products."

Solo Artist:

- "Easy navigation of the website including check out and editing my basket."

* A comment was made regarding the sign up button on the login page, which has been changed.

Engineer:

- "Being able to see a picture of each item when browsing. Being able to see other customers ratings of a product."

#### Q3 - What other information might you be looking for?

Drummer:

- "Songs recorded at that studio."

Solo Artist:

- "Are there any refreshments on site to buy or free i.e. bottled water? Is there parking outside?"

Engineer:

- "Filters to see if there are items on sale"

#### Q4 - Would you use this site?

Drummer:

- "Yes."

Solo Artist:

- "Yes, definitely."

Engineer:

- "Yes, to book rehearsals and recording space, or buy new strings to record with."

#### Q5 - Why?

Drummer:

- "Rehearsal space is relatively cheap and local."

Solo Artist:

- "Suitable for musicians."

Engineer:

- "Rehearsing in the studio is great for practicing in peace without being disturbed. It’s also good to get used to playing inside a studio room before recording."

#### Q6 - What changes could be made?

Drummer:

- "Everything seemed fine as it was!"

Solo Artist:

- "I would like a back button for the recording and rehearsal room info pages."

Engineer:

- "If more variety of brands of strings, capo’s etc, it would be good to filter by brand."

#### Q7 - How did you find the hiring of the sessions, and adding them to cart? Was it as smooth as it should be or were there anomalies?

Drummer:

- "Seemed to work as expected."

Solo Artist:

- "Seemed to work very well."

Engineer:

- "Everything worked exactly as expected."

#### Q8 - Did you receive an email? Did it contain the correct information?

Drummer:

- "Yes to both."

Solo Artist:

- "Yes and yes."

Engineer:

- "I received and email and everything was correct."

### Competitor Review

What other music studios are there in Birmingham?

#### The Oxygen Rooms

The [Oxygen Rooms](https://theoxygenrooms.com/) are a studio located on Barr St in Hockley, on the edge of Birmingham City Centre.

Pro's

- The website is very professional, showcasing fantastic equipment in it's images.

- The header and footer makes the site easy to navigate.

- The contact info is reasonably sized, responsive and informative.

Con's

- The first thing I noticed is there is no favicon, seems like a small issue but this it what also appears on google search, which looks like an illegitimate site.

- Then I noticed the colour scheme throughout the site. All of it is black and white. Although this does look professional it's limiting itself on how welcoming it can be and how it could stand out with colour.

- There is a div on the rehearsals page that doesn't resize with the text, meaning at certain sizes some of the text isn't visible.

<img src="/media/readme-images/oxygen-con.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

- The socials link in the navbar doesn't list socials, but instead takes the user to Instagram without any indication that it is about to do so. The user is no longer on the Oxygen Rooms website.

- You cannot book or hire online at all.

- There is no information about the engineers provided.

#### Pirate.com

[Pirate Studios](https://pirate.com/en/locations/birmingham/) is located on Upper Trinity St in Birmingham.

Pro's

- There are lots of welcoming videos and images showcasing the capabilities of the studios.

- There is a lot of information on this website for the user.

- The equipment information is extensive.

<img src="/media/readme-images/pirate-pro-1.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

- The booking system is effective and works well.

<img src="/media/readme-images/pirate-pro-2.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

Con's

- The images and styling of the site are not very professional.

<img src="/media/readme-images/pirate-con.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

- The links don't have hover qualities, and some don't change the cursor to a pointer, so it's not certain what you are clicking on.

- The use of colour is very strange. Most of the text areas are black and white, and then there are rendom areas of the site with completely random colours thrown in, no scheme at all.

- Really long events and workshops page, no back to top button.

- Navbar is very complicated, there are way too many subchoices.

#### Robannas Studios Birmingham

[Robannas Studios Birmingham](https://www.robannas-studios.co.uk/) is located on Cliveland St, Birmingham.

Pro's

- They have a meet the team section which is friendly looking.

- They have a section explaining some of the celebrities they've worked with, which adds to their credibility.

- Lots of information on really cool looking previous projects.

Con's

- The first thing I noticed is the navbar and header are not responsive. This is the same with every element throughout the site.

<img src="/media/readme-images/robannas-con-1.png" width="50%" alt="Homepage Wireframe" style="display: inherit; ">

- The use of colours and the image of the girls make the website seem on first impression to be for kids, it's not very professional for a recording studio to have parties.

- The footer information is off-screen.
- None of the links have hover attributes.

- Random social links to the right of the navbar.

- Some of the navbar links take you to a completely different site without warning.

### Roadmap

This roadmap indicates the importance and viability of specific opportunities.

| Opportunities/Problems | Importance | Viability |
| ---------------------- | ---------- | --------- |
| Information on engineers | 4          | 5         |
| Information on rehearsal room equipment | 5          | 5         |
| Artists worked with section | 4          | 5         |
| Products page with respective filters and sorts | 5          | 5         |
| Previous order information | 3          | 4         |
| Videos promoting studio | 5          | 0         |
| List of equipment used in studio itself | 3          | 3         |

## Features

### Existing Features

#### Navigation Bar

- The navbar is made of three mini navbars. Two for the main logo, user-options and cart bar, and one for the five main links.
- The first main logo navbar is for big screens, and contains the longer logo, and the two icons anchors to the right.
- The second main logo navbar contains four small icons with similar width, height and hover attributes. Clicking on the user-options ensures the toasts are closed.

<img src="/media/readme-images/navbar-1.webp" width="100%" alt="The Navbar" style="display: inherit; ">

<img src="/media/readme-images/navbar-2.webp" width="10%" alt="The Navbar" style="display: inherit; ">

#### Footer

- The left part of the footer contains the address of the studio
- The middle is the copyright information and contact telephone.
- The right contains the three main social media links.

<img src="/media/readme-images/footer.webp" width="100%" alt="The Footer" style="display: inherit; ">

#### Logo

- The larger Ascension logo has spaces between the letters to make it more grand and spacey.
- The smaller one is the same Raleway font and Styling, with a circular black background.
- Both logos have a slight font shadow beneath.

<img src="/media/readme-images/logo-large.webp" width="50%" alt="Larger Logo" style="display: inherit; ">

<img src="/media/logo-small.png" width="50%" alt="Smaller Logo" style="display: inherit; ">

#### Index Features

- The homepage contains a main message for any user unsure about what the company does, the messages explains the relation to music and how this application can be used to help elevate your music career.
- The three main buttons allow the user to visit the homepage of the three main apps, record, rehearse and products.
- The Little Strings section contains a link to my previous project, which is also musically themed.

<img src="/media/readme-images/index.webp" width="50%" alt="Index Page" style="display: inherit; ">

#### About Us

- Main paragraph is within a turquoise container on the main image, this contains information of the origin of the company.
- The contact us section contains the opening hours, email, phone number and address aswell as giving a visual image via iframe of where the studio is.

<img src="/media/readme-images/about-us.webp" width="50%" alt="About Us Page" style="display: inherit; ">

#### Record Main

- turquoise section same layout as about us information on about us page.
- Artists we've worked with contains a little bio of three local-to-Birmingham artists, which re-organises when opened on mobile into a singular column design.
- The meet the engineers page contains images of the three engineers and a bio with the same layout as the artists previously mentioned.

<img src="/media/readme-images/record-main.webp" width="50%" alt="Record Page" style="display: inherit; ">

#### Rehearsal Main

- turquoise section same layout as about us information on about us page.
- Different types of rooms section contains information on the equipment provided in each room, aswell as an image of each one.

<img src="/media/readme-images/rehearsals-main-1.webp" width="50%" alt="Rehearsals Page" style="display: inherit; ">

#### Products page

- Each product has their own card, creating using a for loop these cards contain all the relevant information aswell as links to edit and delete them and add them to cart. The quantity boxes allow the user to select more or less of the same item.
- The filters allow the user to list the same items currently being shown in a different order, by price or rating.
- Entering this page from the links created across the site views the page in different ways. For example, clicking record and then all studios will give the same products page with studios only. The page title will be STUDIOS and the colour will be gold. Clicking rehearsals instead provides lightblue and the relevant title. Arriving using the strings link will change the title but not the colours of the page.

<img src="/media/readme-images/products.webp" width="50%" alt="Products Page" style="display: inherit; ">

#### Product Information

- On larger screens the image is on the left and the information and buttons on the right.
- On mobile, there again is a singular column, the image above the information above the buttons, all centralised.
- On hire room pages there is also a datepicker which triggers five radio buttons with hour long slots attached.

<img src="/media/readme-images/product-information.webp" width="50%" alt="Products Information Page" style="display: inherit; ">

#### Add a product form

- The form within this page is created using the forms.py.
- The image file fields generate the image name automatically but aren't easy to style. So I've hidden them behind easy to style ones and added event listeners so when you click the top button it triggers the underneath button.
- There are two relevant images to the right of the form, they disappear on smaller screens.

<img src="/media/readme-images/add-product.webp" width="50%" alt="Add a Product Form" style="display: inherit; ">

#### Edit a product

- The edit page is very similar to the add a product page, except the javascript keeps the information invisible until an option is selected and searched, meaning the form only shows on this page if it contains information.
- Coming to this page from a products description will automatically contain that products information.

<img src="/media/readme-images/edit-product-1.webp" width="50%" alt="Edit Product Page" style="display: inherit; ">

<img src="/media/readme-images/edit-product-2.webp" width="50%" alt="Edit Product Page" style="display: inherit; ">

#### Cart page

- The product image is on the left, reading right we then have the line item information and quantity along with a subtotal. This is displayed in a singular column on mobile devices.
- This page also has an empty cart button, which first displays a modal ensuring you want to empty your cart.
- There are buttons to take you back to products and take you to the checkout page.

<img src="/media/readme-images/cart.webp" width="50%" alt="Cart Page" style="display: inherit; ">

#### Checkout page

- The checkout page displays the pre-filled billing info on the right. If there is no pre-written info, updating this and selecting the radio at the bottom will store this information to the user.
- The Order Summary section contains all the products you are about to order, along with the quantities.

<img src="/media/readme-images/checkout.webp" width="70%" alt="Checkout Page" style="display: inherit; ">

#### Checkout Success

- There is a loading spinner that is displayed whilst the payment is going through.
- The about section is similar to what has been used before, turquoise background on an image.
- Order information is displayed below, when we arrive here from the profile page, the toast message lets the user know this is an old order.

<img src="/media/readme-images/check-succ.webp" width="50%" alt="Checkout Success Page" style="display: inherit; ">

#### Profile page

- Billing information is included on the left, previous orders on the right.
- The order numbers are truncated so they don't take up too much unnecessary space, and they are links to the checkout success page for that order.

<img src="/media/readme-images/profile.webp" width="70%" alt="User Profile Page" style="display: inherit; ">

### Features Left to Implement

- Videos promoting the studio in use. This would be powerful on the index page and it wouldn't be difficult to get great images from a professional music studio.
- Engineers accomplishments and songs they've worked on.

## Testing

You can view all testing in [this document.](https://github.com/ryanmcnally93/ascension/blob/main/testing.md)

### Fixed Bugs

1). The first issue I had was linking my products CSS stylesheet. I wrote the URL for the static CSS file but could not locate it, I kept receiving a 404 error.

I contacted tutor support and before they had a chance to help me I reloaded my workspace and the URL worked. I believe that Code Anywhere must have timed out in some way without letting me know, as refreshing the workspace completely fixed the issue.

2). I had an issue when creating the select element on the products page. Initially I attempted to change the content of the page only using javascript, but struggled with understanding how to find the sort and direction values and enter them into the URL. I fixed this by going back over the lessons and finding the tutorial on the postload js for the products page.

3). One of the biggest challenges I gave myself really was with the add to cart button functionality on the product page.

<img src="/media/readme-images/bug-3.webp" width="80%" alt="The add to cart and quantity buttons" style="display: inherit; ">

I needed the page to know which product specifically I was increasing the quantity of. I also needed the page to either stay where it was or when it loads, quickly travel back to where the user was to add a bit of smoothness to the site.

To achieve this I altered the redirect URL to include the product's specific ID so when the page loads again it takes the user back to the product.

I also added an invisible field with the name 'quantity' and the value '1', which is only accessible when the quantity box (also called quantity) is not available. By doing this the view will always have access to a quantity value. By setting the invisible one to '1', the view will simply add this 1 to the cart when it runs the 'cart*procuct_id* = quantity' piece of code.

The increase and decrease buttons also have their own names, which trigger different actions in the view for adding to the quantity and taking away. Once the product is in the cart it won't call on the invisible quantity box again until returned to 0.

4). I could not access the cart variable in jinja to see whether the product was already inside.

I tried adding cart_list to product_information views.py so I could access it as a list, as the list() function didn’t work in jinja. This returned [‘2’]. As I attempted to check that against my product.id, it wouldn't work as they were different types. I attempted product.id|string but this failed to work too.

With help of a tutor we realised that the product id was integer but the dictionary values in cart_list were string. I created a string version of my product.id in product information.html which I then used in the html document.

This helped with the product_information.html but not the product.html.

As I was using a for loop to go through all the products, I tried to create a function that returns the product id’s needed but this didn’t work. With help again from a tutor I created a custom_filters.py which accomplishes what I was trying to achieve within the earlier function.

This Custom Filters document lives in the product apps template tags and helps the page search through the current cart for information like item_id, quantity and subtotal.

5). At one point my toasts were not rendering. This took me an hour to find the cause of the issue, annoyingly, the Bootstrap toast class was adding opacity: 0.

6). I noticed that if toasts were open and the user clicked on user-options, it opened up behind the toast, when it should really also close the toast.

I found a piece of code by Richard Ash on Slack, that closes the toast and placed this within a function that is called when the user-options anchor is clicked.

7). When creating the add and edit product management pages, I had the following error.

<img src="/media/readme-images/bug-7.webp" width="80%" alt="The template could not be found" style="display: inherit; ">

Bootstrap4/uni_form.html template does not exist, after a lot of online searching I found the solution was to install 'bootstrap4crispyforms' and add it to installed apps, which worked.

8). When setting up Stripe payments, I had the payments going through succesfully on the night, but the next day, they refused to work. I spent hours messing with the code and trying to work out why my payment intents and payment success webhooks were coming back with a red X rather than a green tick.

<img src="/media/readme-images/bug-8.webp" width="70%" alt="Payments failing in Stripe" style="display: inherit; ">

I tried setting env.py variables rather than importing and exporting into my terminal and deleting and rewriting webhooks, looking at differences in documents.

I eventually asked for the support of a tutor, who showed me the port was not public so stripe couldn’t access the web hook. I had made it public the night before but completely forgotten about needing to do it the next day, needless to say this mistake won't happen twice!

9). I had an issue with the info toasts displaying as success toasts. I tried looking at the views messages and there were no spelling errors, the toasts html documents contained the correct information too.

I realised it was the if statement within the base.hmtl that had the messages success.html loading, which I changed and fixed the issue.

<img src="/media/readme-images/bug-9.webp" width="70%" alt="The if statement that was wrong initially" style="display: inherit; ">

10). I had an issue where if you added an item to cart, then signed in, it showed the items in your cart within the success toast that is only mentioning the successful sign in.

I made 'on_profile_page' true on index page as I couldn't think of a scenario where the quantities of an item will change when entering the index page, this information is not important so doesn't need to be shown.

11). I realised that items with the ID of 'my-account' and 'cart' are in the page twice, one is hidden and one isn’t, so I had to rewrite javascript to target the specific elements with the hover qualities desired.

12). I spent a lot of time trying to format the order.date in Jinja. 

I tried .strftime, |strftime and strftime('&d-&m-&Y'), along with changing variables within views.py. As the order was being created using a for loop, this couldn't be solved in views.py.

I finally managed to find a way to format date in Jinja2, using 'order.date|date: "Y-m-d"'.

13). I realised on checkout success that the order line items for hire rooms needed to increase when the date was different but product ID the same.

The quantity also returned 0. In order to fix these issues I needed to save the line items differently in the view for items with product.is_hire_room equal to true.

I made quantity equal to the 'length' or amount of the dictionary's values. The date is equal to the item's key.

14). Custom Filters on the product and cart pages were returning the incorrect quantities. This was incredibly hard to figure out but I did in the end find a solution.

I first had to decipher if the product was a hire room, then find the amount of times there were to the date that had been passed in. This worked for the cart page.

On the products page I needed to add that quantity to the other cases of the same product_id. This meant that on products page it showed the quantity of all the cases of this item currently in the cart.

15). I had a bug where rehearsal 1's image wouldn't show in toasts. Checking the toast_success.html I realised I had an if statement for hire rooms. This if statement will always hit main image and go no further, except for this one hire room which doesn't have a main image. The image url had .url at the end. Removing this fixed the issue.

16). Everytime I saved the details of the user when checking out, Stripe was adding brackets and commas to each field.

This was tricky to figure out, but I solved the issue by adding .strip("(',)") to the end of each field when being saved.

17). Finding the times of a hire room and displaying them in the admin was a pain. I have the time dictionary within a date dictionary within a session_datetime dictionary within a cart dictionary!

I fixed this by using a for loop to go through the dates and using that date variable to drill into the times section. I then used ", ".join() around the answer to turn the dictionary keys into a list with commas in-between and no brackets. These display in the orders admin section nicely now.

18). I tried to create a session with booked sessions inside, this created massive issues. I had to save the product id, date and time within a dictionary and then try and access and manipulate this date throughout.

<img src="/media/readme-images/unfixed-1.webp" width="70%" alt="The code I used" style="display: inherit; ">

I quickly realised this approach wouldn’t be practical in the real world as this data would need to be saved onto a database rather than within a local session which would be deleted.

<img src="/media/readme-images/unfixed-2.webp" width="70%" alt="The code I used" style="display: inherit; ">

I instead just allowed users to checkout with the selected dates and times added to their products, without checking for availability. I did add some functionality to check for past dates or dates that exceed two weeks, and returned an error for these.

After giving this issue some time and waiting until the end of my project, I have decided to build on this and add some python and javascript to return all the orders to the template and sift through the dates and times to only allow users to select and book available times. This took a lot of thinking and manipulating, but I have commented through the steps within the products views.py for product_information and the product_information.js file.

### Unfixed Bugs

1). I need to create a check as an order goes through to ensure that in the time it has taken for someone to book a session, somebody else hasn't already booked the same product, date and time. At the moment if two users book at the same time, they will have the same session!

2). By default if a user clicks on a date that is already in their cart, the sessions in their cart should also be disabled. We do have a block in place for after the form is submitted but for ease of use it should really be greyed out.

### Responsive Design

#### Navbar

- I created a smaller logo and gave it and the toggler specific hover qualities so the user knows when they are about to click something important.
- I removed padding left from user-options to prevent moving to next line.

<img src="/media/readme-images/navbar-responsive.webp" width="70%" alt="Navbar responsiveness" style="display: inherit; ">

#### Footer

-  I made the middle writing smaller, eventually left-aligning it and making the writing on the left disappear.
- Initially the social media icons were too large when 430px, and the small logo and user-options collided. Buttons got too small for their text, sorted I fixed those.

#### Product Information

- I've made the information a flex-column on small and medium devices. Adding a section for the hire-rooms' specific information and centralised the contents on smaller devices.

#### Product Page

- I made the page slightly longer to account for text spilling over, and changed the card width’s so not too wide or thin on mobile devices.

#### Add & Edit Products Pages

- I made images disappear on smaller devices, and made the search bar col-12 on smaller devices with the button underneath, so you can read more of the product name.

#### Profile Page

- Added margin bottom to longer page and gave custom margin bottom so order history and billing was in line.

#### Cart Page

- Added padding to product name on medium screens as before it was touching the image.
- Changed flex-direction on mobile.
- Placed quantity box and price on same line and subtotal title to that price so it’s clear as to what is happening.
- Total box has width limit so the border looks more in line with objects above.
- Centralised buttons at bottom of page.

#### Checkout Page

- Similar to cart, make into a singular column, centralise information, Image size changes.

<img src="/media/readme-images/checkout-responsive.webp" width="50%" alt="Checkout responsiveness" style="display: inherit; ">

#### Other Pages

- Used the same layout on record page and engineer page for three engineers and artists. This kept things simple when made smaller, no changed needed to be made.
- Page information has been contained in rows, and I've made the length of header container to 700px to contain main images and centralised the rows.
- Added maximum width on message container for mobile devices.

## Credits

### Code

- The HTML, CSS and JS code for the slideshows on the Product Information pages were originally taken from [W3Schools.](https://www.w3schools.com/howto/howto_js_slideshow.asp) I later changed the styling and layout to better suit the site.

- On my checkout success page I needed to render the date in a smaller format for smaller screens. Unfortunately I couldn't find a way to udse strftime within Jinja, but found this alternate solution on [Stack Overflow](https://stackoverflow.com/questions/44570965/django-error-could-not-parse-the-remainder-y-m-d-from-post-datedate) - Author 'Daniel Roseman'.

- I used [W3Schools](https://www.w3schools.com/howto/howto_css_hide_arrow_number.asp) to remove arrows on the searchbar as they had no hover quality and looked messy.

- I used this slack post by [Richard Ash](https://app.slack.com/client/T0L30B202/search?cdn_fallback=2) to close toasts when user-options is selected.

- I used this Slack Overflow solution by [Jezen Thomas](https://stackoverflow.com/questions/18739937/how-to-keep-footer-at-bottom-of-screen) to produce a sticky footer that stays at the bottom of the page.

- I used the second solution on [this Stack Overflow page](https://stackoverflow.com/questions/16041232/django-delete-filefield) to install django cleanup, which deletes a file if it is removed from a form, like the images that are installed when adding and editing a product. It also deletes the image from the project roots when you delete the product. 

- I used this code from Stack Overflow by [Constantin](https://stackoverflow.com/questions/58352814/how-to-change-formatting-of-stripe-card-element-based-on-viewport-size) to target the Stripe card element when screen size changes through an event listener in JavaScript.

#### Code Institute's Boutique Ado

Due to the fact I learned how to integrate Stripe and create an E-Commerce site from Code Institute's lessons on their project 'Boutique Ado', there are a number of similarities and in some cases, the same code.

- Navbar design has similarities.
- The if statement within base.html that renders the 'messages' is the same.
- Toasts are setup the same, although there are changes I have made.
- Products Category Model is the same.
- Products admin.py is similar.
- Sort and Direction in products views.py & JavaScript to make it work almost identical.
- The for loop in cart contexts is similar to their 'bag contexts' loop.
- The Checkout apps models functions are similar.
- Checkout signals.py identical.
- Checkout template has exact code in places
- Views forms and admin for checkout.
- The Stripe Elements.js in the checkout app. This JavaScript was originally copied and pasted, differences have since been made.
- Checkout_success view almost same.
- Webhook handler has been copied and pasted.
- Webhooks.py has been copied and pasted.
- The profiles model is very similar.
- Profiles forms.py is almost the same.
- Products forms.py is very similar, with changes.

### Web Tools

- I used [Contrast Checker](https://webaim.org/resources/contrastchecker/) to make sure my headings were visible against their background colours.
- I used [Re-Sizing Images](https://www.simpleimageresizer.com/upload) to re-size images that were unnecessarily large.
- I used this [Webp Converter](https://ezgif.com/png-to-webp) to convert all images to webp format.
- And then this [Image Compresser](https://tinypng.com/) to make their file size smaller.

### Media

#### Product Descriptions and Images

- Shop Products 1-5 (SP01-SP05) - Descriptions obtained from [Gak](https://www.gak.co.uk/)
- SP01 Image - Obtained from [Amazon](https://www.amazon.co.uk/Ernie-Ball-Regular-Slinky-Nickel/dp/B00CAV0TRQ/ref=sr_1_5?keywords=Ernie-Ball&qid=1694685948&sr=8-5&th=1)
- SP02 Image - Obtained from [Amazon](https://www.amazon.co.uk/Ernie-Ball-Skinny-Bottom-String/dp/B0002PBS68)
- SP03 Image - Obtained from [Amazon](https://www.amazon.co.uk/Ernie-Ball-Electric-Guitar-Strings/dp/B0002M6CW6?th=1)
- SP04 Image - Obtained from [Strings Direct](https://www.stringsdirect.co.uk/products/ernie-ball-2213-mega-slinky-10-5-48-electric-guitar-strings)
- SP05 Image - Obtained from [Amazon](https://www.amazon.co.uk/Ernie-Ball-Skinny-Electric-Strings/dp/B083LML2N3?th=1)

- Descriptions and Images were obtained from the following links
- SP06 & SP07 - [Gear4Music](https://www.gear4music.com/Guitar-and-Bass/Electric-Guitar-Strings-by-Gear4music/2UN?utm_campaign=surfaces_across_google&srsltid=AfmBOooFs_A2IJIAhgymYyYleBEBTgKCYifp_OqIr6OIaCCyGNooOwDTRto)
- SP08 - [Google Shop](https://www.google.com/search?q=Gear4music+Light-Heavy+Strings+10-52&sa=X&sca_esv=564766799&biw=1242&bih=821&tbm=shop&sxsrf=AM9HkKkQtiEg6S4b77i6SWF65EMNDOeZ_A%3A1694544401167&ei=EbIAZfDgCKKohbIPw56rqA0&ved=0ahUKEwiwrdjo3aWBAxUiVEEAHUPPCtUQ4dUDCAg&uact=5&oq=Gear4music+Light-Heavy+Strings+10-52&gs_lp=Egtwcm9kdWN0cy1jYyIkR2VhcjRtdXNpYyBMaWdodC1IZWF2eSBTdHJpbmdzIDEwLTUyMgUQIRigAUiOAlAAWABwAHgAkAEAmAFxoAFxqgEDMC4xuAEDyAEA-AEC-AEBiAYB&sclient=products-cc#spd=1257663784045161876)
- SP09 - [Gear4Music](https://www.gear4music.com/Guitar-and-Bass/3-Pack-of-Bass-Guitar-Strings-Set-by-Gear4music/312E?origin=product-ads&gclid=Cj0KCQjwmICoBhDxARIsABXkXlKJ2aT0vzqAYwfu2NUPfQ17tI36fkPQieIm0K9O5foQ-DLbQfh5fbYaAq1nEALw_wcB)
- SP10 - [Amazon](https://www.amazon.co.uk/Tiger-Music-GACAPO2-Capo-Guitar/dp/B004PA5T5M?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A3P5ROKL5A1OLE&th=1)
- SP11 - [Strings Direct](https://www.stringsdirect.co.uk/products/shubb-c1-electric-acoustic-guitar-capo-nickel?variant=45003259150630&currency=GBP&utm_source=google&utm_medium=cpc&utm_term=&gad=1&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtiGg_2E9QSM_BykjuOj__voE1lRAVrudXN2hnnL1O5EUxQ9zBmw2BRoCIS8QAvD_BwE)
- SP12 - [Gear4Music](https://www.gear4music.com/Drums-and-Percussion/5A-Wood-Tip-Drumsticks/WD?utm_campaign=surfaces_across_google&srsltid=AfmBOor9aOPKz97FXgxta1N2v1gz78yyqYT5ET4WvzElqkbMhFFiil4zeVI)
- SP13 - [ADCDrums](https://adcdrums.co.uk/products/bopworks-40s-swing-classic-drumsticks/?utm_source=Google+Shopping&utm_medium=cpc&utm_campaign=GMerchant)
- SP14 - [Gear4Music](https://www.gear4music.com/G4M/Stagg-SMC10-10m-XLR-to-XLR-Microphone-Cable-Black/1W46?origin=product-ads&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtmOJQ_gZ1F_Qj40cH5zuTxYPaXyRow1-S6nP5IyVQRASTnHD6EnP_xoCQIkQAvD_BwE)
- SP15 - [Amazon](https://www.amazon.co.uk/Urbanphonics-Microphone-Balanced-Recording-Amplification/dp/B08BFKM22Z/ref=asc_df_B08BFKM22Z/?tag=&linkCode=df0&hvadid=427962886940&hvpos=&hvnetw=g&hvrand=16882899087854239772&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007136&hvtargid=pla-930750179222&ref=&adgrpid=99954789552&th=1)
- SP16 - [Music Room](https://www.musicroom.com/fender-deluxe-10-straight-angle-instrument-cable-tweed-fnd0990820091?glid=gb&CAWELAID=120075890000278513&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtuoPSVUlAUTxbAbGEK5Piq2b6g9pwG2L5rLElgEPmMowvz_PAF8K9RoCs2cQAvD_BwE)
- SP17 - [Global Audio Store](https://www.global-audio-store.fr/en/31184-ibanez-si20-jack-guitar-cable-2-straight-jacks-6-10m.html?gclid=CjwKCAjw3oqoBhAjEiwA_UaLtg7yFn2-DqoBOnQgDYEW31mNYW0mfb81gQKcQHP8TlhXaYWa5WTeZRoCq8oQAvD_BwE)
- SP18 - [Gear Geek](https://geargeek.co.uk/aux-cable-1m/?sku=AUX_CABLE_1M/EAU-42291&utm_source=googleshopping&utm_medium=cse&srsltid=AfmBOoqw8O2QFOhTUOklzoyoSsWSw3-dWIpTwBj0E7VS5xpOYmmlMlZUL0M)
- SP19 - [Music Room](https://www.musicroom.com/dunlop-standard-0-6mm-plectrum-12-pack-jd418p60?glid=gb&CAWELAID=120075890000278072&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtrj-Qm6woSDqRudrhKSFVrlkAyvueFlzFTS2lUEfRKUIVOyIZsCQJBoC1SIQAvD_BwE)
- SP20 - [Reverb](https://reverb.com/uk/p/fender-celluloid-shape-medley-picks-medium-8?hfid=35452792&utm_source=google&utm_medium=cpc&utm_campaign=18354914807&utm_content=campaignid=18354914807_adgroupid=_productpartitionid==merchantid=134269987_productid=35452792_keyword=_device=c_adposition=_matchtype=_creative=&gclid=CjwKCAjw3oqoBhAjEiwA_UaLtpc87w6KYxJQJsh9-DQaH2WSTSzSi7NWPTABiEGd09l9sl1ed5Y4GhoC44QQAvD_BwE)
- SP21 - Image only [Ebay](https://www.ebay.co.uk/itm/404433500745?chn=ps&_trkparms=ispr%3D1&amdata=enc%3A1t4io50yvRNSYez1iIz9mCg2&norover=1&mkevt=1&mkrid=710-134428-41853-0&mkcid=2&mkscid=101&itemid=404433500745&targetid=1647205088280&device=c&mktype=pla&googleloc=9045502&poi=&campaignid=19926849521&mkgroupid=147378848803&rlsatarget=aud-1415330310908:pla-1647205088280&abcId=9311021&merchantid=5077338291&gclid=Cj0KCQjwtJKqBhCaARIsAN_yS_nu5AH8tdyslRaPYhP4d--WK8Hp7OKQ-ar1q2VQcHrRN7ks4r95e6oaAswwEALw_wcB)
- SP22 - [Amazon](https://www.amazon.co.uk/Cristal-Original-Ballpoint-Medium-Point/dp/B000I5ZK2U/ref=asc_df_B000I5ZK2U/?tag=googshopuk-21&linkCode=df0&hvadid=207961469242&hvpos=&hvnetw=g&hvrand=2487639748670704103&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007136&hvtargid=pla-406179071418&th=1)
- SP23 - [Staples](https://www.staples.co.uk/office-supplies/writing-supplies/ballpoint-pens/black-medium-ballpoint-pens-pack-of-50-0052501-nb/?gclid=CjwKCAjw3oqoBhAjEiwA_UaLtkjbFprEykNyPWOIjRvVbY8IUCIFxmfIH2HW8w9C9SMOeDb89vR0PxoCzaQQAvD_BwE)

The following hire rooms images were obtained from these links, along with some of the descriptions, which I have altered to tailor to my fake products.
- SP24 - [Milco Studios](https://milocostudios.com/studios/summerfield-studios/image-gallery/)
- SP25 - Image 1 - [Milco Studios](https://milocostudios.com/studios/jbj-studio/overview/)
- SP25 - Image 2 - [Milco Studios](https://milocostudios.com/studios/jbj-studio/image-gallery/)
- SP26 - [Milco Studios](https://milocostudios.com/studios/decoy-studios/studio-gallery/)

The following descriptions were written by me, these links are to the images only.
- SP27 - [Acoustic Booth - Studio Box](https://www.acousticbooth-studiobox.com/soundproof-practice-booth.html)
- SP28 & SP29 - [Pirate Studios](https://pirate.com/en/rehearsal-studios/)

- No media image obtained from [ncenet.](https://www.ncenet.com/no-image-png-2)

#### Artist Descriptions and Images

- Call Me Unique's description - [Call Me Unique.](https://www.callmeunique.com/about)
- Call Me Unique's Image - [PRS Foundation](https://prsfoundation.com/grantees/women-make-music-call-me-unique/) - No credited author.
- Lady Sanity's description - [PRS Foundation](https://prsfoundation.com/grantees/women-make-music-lady-sanity/)
- Lady Sanity's Image - [Birmingham Mail](https://www.birminghammail.co.uk/whats-on/music-nightlife-news/who-lady-sanity-brummie-rap-14514351) - No credited author, although Neil Elkes was mentioned on earlier image.
- I wrote Yatez's description, but the image was obtained from [Linktr](https://linktr.ee/yatez).

#### Engineer Images

These images were obtained from pexels.com.
- Alicia Green image author - Tarzine Jackson.
- Adam Moore image author - Tyler Sherrington
- John Polter imag author - Simon Robben

#### Title Background Images

- Index-main Image obtained from [Yelp](https://www.yelp.com/biz_photos/soundxtreem-studios-atlanta-2?select=xRsIAvaYhLXXWbyZEoJ_MQ) - SoundXtreem Studios Credited.
- About-main image obtained from [Pexels](https://www.pexels.com/) - Author 'Cottonbro Studio'.
- Shop-main image obtained from [Pexels](https://www.pexels.com/) - Author 'Cottonbro Studio'.
- Record-studio-main image obtained from [Pexels](https://www.pexels.com/) - Author 'Pixabay'.
- Rehearsals-main image obtained from [Pexels](https://www.pexels.com/) - Author 'Wendy-Wei'.
- Login page image obtained from [Pexels](https://www.pexels.com/) - Author 'WallaceChuck'.
- Logout page image obtained from [Pexels](https://www.pexels.com/) - Author 'Cottonbro Studio'.
- Register page image obtained from [Pexels](https://www.pexels.com/) - Author 'Eduardo Dutra'.
- Add a product image one obtained from [Pexels](https://www.pexels.com/) - Author 'Caleb Oquendo'.
- Add a product image two obtained from [Pexels](https://www.pexels.com/) - Author 'Cottonbro Studio'.

### Acknowledgements

- I'd like to thank my tutors from City of Bristol College, Ben Smith and Pasquale Fasulo for their support.
- Jubril Akolade for mentoring me through the three stages of completion.
- The Code Institute technical team for their help with some of the bigger issues I faced.

This readme.md has been spellchecked using the spell checker extension for Chrome.

All documents within this repository have been formatted using "Prettier".
