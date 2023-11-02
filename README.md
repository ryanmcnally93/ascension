# Ascension

<!-- IMAGE -->

This is a Django web application for Ascension, a music studio based in Birmingham. Languages used include HTML, CSS, JavaScript and Python, created using Django Crispy Forms, All Auth, Stripe, Pillow & Bootstrap.

Thie project allows users to book studio time with engineers or rehearsal rooms for practicing musicians/bands. It also has a small shop which is situated in the foyer, where musicians can buy strings, capos, and other small instrument parts.

The web application allows the creator to create more listings in the products section, and more studios, sound engineers and rehearsal rooms.

<p align="center">

<img src="https://img.shields.io/github/stars/ryanmcnally93/project-four-ascension?style=social" style="max-width: 100%; margin: 0 10px 10px 0;" alt="Stars">

<img src="https://img.shields.io/github/repo-size/ryanmcnally93/project-four-ascension" style="max-width: 100%; height: 20px; margin: 0 0 10px 10px;" alt="Size of repo">

<br>

<img src="https://img.shields.io/github/issues-raw/ryanmcnally93/project-four-ascension" style="max-width: 100%; height: 20px margin-right: 10px;" alt="Open issues">

<img src="https://img.shields.io/github/last-commit/ryanmcnally93/project-four-ascension?color=green&style=for-the-badge" style="max-width: 100%; height: 20px; margin-left: 10px;" alt="GitHub last commit">

</p>

## Deployment

<!-- To deploy my first Heroku project, I followed the steps set by Code Institute.

- Create an account on ElephantSQL
- Create new instance and copy database URL
- Create a Procfile and requirements.txt file
- Add an if statement to ensure SQLAlchemy can read my external database.
- Create new app on Heroku
- Enter config vars, including the copied URL
- Click on deploy, connect to github, find the repository
- Click Deploy Branch
- Once that is done, click more, and run console.

It was importing the database from torquay_sunday_league that first provided issues.

My requirements.txt hadn't created an instance for the 'requests' module which needed to be installed. I checked the version I had and provided it in the file.

- I tried again and it worked, after this I opened the app and entered the teams data into the database. -->

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
| Promote professional looking studios and engineers.          | Shadp edges, blues and dark silvers used, looks slick. |
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

- Should be able to view products and pages as norma.
- User-options should be 'login' or 'register' only.
- Should be able to add to cart as normal.
- Typing url for disallowed pages should take user to the login page.
- Checkout page requires URL to assure unregistered user cannot make purchases.

#### Logged in User

- Should extend all the same privileges as the unregistered user.
- Should still not allow you to accees the Add and Edit product pages.
- Should be able to checkout using test card data.
- Should be able to access Profile page, with order history.
- Should be able to save billing info.

#### Administrator

- Should extend all the same privileges as the logged in user.
- Should have access to add and edit products pages.
- Should be able to edit and delete products on products page and product information pages.
- Should be able to delete products.

### Design Choices

The website needs to look professional and high tech, we want customers to feel like this is a high end studio that knows their craft. We want thea dark blue environment associated with being in a studio, I'm going for electric blue to stay relative, with sharp edges.

#### Fonts

- I decided to use the 'Raleway' font as it has character in lowercase but has a very professional look in uppercase. This has been used across the whole web-application.

<img src="/media/readme-images/fonts.webp" width="50%" alt="The fonts used" style="display: inherit; ">

#### Icons

- The user icon is used within the navbar for the user options, from logging in to viewing your profile.
- The cart has a shopping-cart icon, as does the back to cart button on the checkout page.
- The social media icone are within the footer, with the same styling as the rest of the site.
- Secure payment and complete order have the safety lock icon. So users know this is secure.
- The toast messages have relevant ticks, x's, and warning and information icons.

<img src="/media/readme-images/icons-1.webp" width="50%" alt="Navbar Icons" style="display: inherit; ">

<img src="/media/readme-images/icons-2.webp" width="50%" alt="Footer Icons" style="display: inherit; ">

#### Colours

- I wanted to use an electric blue initially, to give the page a more digital look. I settled in the end for a dark turqoise.
- The main colours are #282C2E, a dark grey colour, and #033A54 the dark turqoise.
- The navbar is turqoise and the footer grey, with the mobile navbar also being grey.
- The primary buttons are turqoise and the secondary buttons are grey, the hover qualities change the buttons main colors with white and the white test to the main color. This is the same throughout.

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

<img src="/media/readme-images/backgrounds.webp" width="50%" alt="Example of a background used" style="display: inherit; ">

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

#### Q1 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

#### Q2 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

#### Q3 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

#### Q4 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

#### Q5 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

#### Q6 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

#### Q7 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

#### Q8 ?

Drummer:

- ""

Solo Artist:

- ""

Engineer:

- ""

### Competitor Review

What other music studios are there in Birmingham?

#### The Oxygen Rooms

The [Oxygen Rooms](https://theoxygenrooms.com/) are a studio located on Barr St in Hockley, on the edge of Birmingham City Centre.

Pro's

- The website is very professional, showcasing fantastic equipment in it's images.

- The header and footer makes the site easy to navigate.

- The contact info is reasonably sized, responsive and informative.

Con's

- The first thing I noticed is there is no favicon, seems like a small issue but this it what also appers on google search, which looks like an illegitimate site.

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

<img src="/media/readme-images/navbar-1.webp" width="50%" alt="The Navbar" style="display: inherit; ">

<img src="/media/readme-images/navbar-2.webp" width="50%" alt="The Navbar" style="display: inherit; ">

#### Footer

- The left part of the footer contains the address of the studio
- The middle is the copyright information and contact telephone.
- The right contains the three main social media links.

<img src="/media/readme-images/footer.webp" width="50%" alt="The Footer" style="display: inherit; ">

#### Logo

- The larger Ascension logo has spaces between the letters to make it more grand and spacey.
- The smaller one is the same Raleway font and Styling, with a circular black background.
- Both logos have a slight font shadow beneath.

<img src="/media/readme-images/logo-large.webp" width="50%" alt="Larger Logo" style="display: inherit; ">

<img src="/media/logo-small.png" width="50%" alt="Smaller Logo" style="display: inherit; ">

#### Index Features

- The homepage contains a main message for any user unsure about what the company does, the messgges explains the relation to music and how tihs application can be used to help elevate your music career.
- The three main buttons allow the user to visit the homepage of the three main apps, record, rehearse and products.
- The Little Strings section contains a link to my previous project, which is also musically themed.

<img src="/media/readme-images/index.webp" width="50%" alt="Index Page" style="display: inherit; ">

#### About Us

- Main paragraph is within a turqoise container on the main image, this contains information of the origin of the company.
- The contact us section contains the opening hours, email, phone number and address aswell as giving a visual image via iframe of where the studio is.

<img src="/media/readme-images/about-us.webp" width="50%" alt="About Us Page" style="display: inherit; ">

#### Record Main

- Turqoise section same layout as about us information on about us page.
- Artists we've worked with contains a little bio of three local-to-Birmingham artists, which re-organises when opened on mobile into a singular column design.
- The meet the engineers page contains images of the three engineers and a bio with the same layout as the artists previously mentioned.

<img src="/media/readme-images/record-main.webp" width="50%" alt="Record Page" style="display: inherit; ">

#### Rehearsal Main

- Turqoise section same layout as about us information on about us page.
- Different types of rooms section contains information on the equipment provided in each room, aswell as an image of each one.

<img src="/media/readme-images/rehearsals-main-1.webp" width="50%" alt="Rehearsals Page" style="display: inherit; ">

#### Products page

- Each product has their own card, creating using a for loop these cards contain all the relevant information aswell as links to edit and delete them and add them to cart. The quantity boxes allow the user to select more or less of the same item.
- The filters allow the user to list the same items currently being shown in a different order, by price or rating.
- Entering this page from the links created accross the site views the page in different ways. For example, clicking record and then all studios will give the same products page with studios only. The page title will be STUDIOS and the colour will be gold. CLicking rehearsals instead provides lightblue and the relevant title. Arriving using the strings link will change the title but not the colours of the page.

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
- The Order Summary section contains all the products you are about to order, along with the quantites.

<img src="/media/readme-images/checkout.webp" width="50%" alt="Checkout Page" style="display: inherit; ">

#### Checkout Success

- There is a loading spinner that is displayed whilst the payment is going through.
- The about section is similar to what has been used before, turqoise background on an image.
- Order information is displayed below, when we arrive here from the profile page, the toast message lets the user know this is an old order.

<img src="/media/readme-images/check-succ.webp" width="50%" alt="Checkout Success Page" style="display: inherit; ">

#### Profile page

- Billing information is included on the left, previous orders on the right.
- The order numbers are truncated so they don't take up too much uneccessary space, and they are links to the checkout success page for that order.

<img src="/media/readme-images/profile.webp" width="50%" alt="User Profile Page" style="display: inherit; ">

### Features Left to Implement

- Videos promoting the studio in use. This would be powerful on the index page and it wouldn't be difficult to get great images from a professional music studio.
- Engineers accomplishments and songs they've worked on.

## Testing

You can view all testing in [this document.]()

### Fixed Bugs

1). The first issue I had was linking my products CSS stylesheet. I wrote the URL for the static CSS file but could not locate it, I kept receiving a 404 error.

I contacted tutor support and before they had a chance to help me I reloaded my workspace and the URL worked. I believe that Code Anywhere must have timed out in some way without letting me know, as refrshing the workspace completely fixed the issue.

2). I had an issue when creating the select element on the products page. Initially I attempted to change the content of the page only using javascript, but struggled with understanding how to find the sort and direction values and enter them into the URL. I fixed this by going back over the lessons and finding the tutorial on the postload js for the products page.

### Unfixed Bugs

### Responsive Design

#### Navbar

- I created a smaller logo and gave it and the toggler specific hover qualities so the user knows when they are about to click something important.
- I removed padding left from user-options to prevent moving to next line.

<img src="/media/readme-images/navbar-responsiveness.webp" width="50%" alt="Navbar responsiveness" style="display: inherit; ">

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

<img src="/media/readme-images/checkout-responsiveness.webp" width="50%" alt="Checkout responsiveness" style="display: inherit; ">

#### Other Pages

- Used the same layout on record page and engineer page for three engineers and artists. This kept things simple when made smaller, no changed needed to be made.
- Page information has been contained in rows, and I've made the length of header container to 700px to contain main images and centralised the rows.
- Added maximum width on message container for mobile devices.

## Credits

### Code

-

### Web Tools

-

### Media

-

### Acknowledgements

-

This readme.md will be spellchecked using the spell checker extension for Chrome.

All documents within this repository will be formatted using "Prettier".
