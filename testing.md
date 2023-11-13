# Ascension Testing

I have tested my web application automatically and manually using Test Driven Development and Behaviour Driven Development.

## Automated Testing

### W3C Validation

#### HTML

All the following HTML documents (which are written using Django templates), have been validated using the [W3C Validator.](https://validator.w3.org/nu/#textarea). All django template lines were taken out to avoid confusion within the validator.

- [base.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/base.html) returned no errors.

- The rehearse app's [home.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/rehearse/templates/rehearse/home.html) returned no errors.

- The record studio's app's [home.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/record_studio/templates/record_studio/home.html) returned no errors.

- [meet_the_engineers.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/record_studio/templates/record_studio/meet_the_engineers.html) returned no errors.

- [profile.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/profiles/templates/profiles/profile.html) returned no errors.

- [add_products.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/templates/products/add_products.html) returned no errors.

- [edit_products.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/templates/products/edit_products.html) returned no errors.

- [product_information.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/templates/products/product_information.html) mentioned that the 'variable' attribute was present and not allowed on the radio inputs, this has now been removed. There was also a div within a 'small' element. I opted to change this to a div.

- [products.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/templates/products/products.html) was the hardest html document to check, as there are so many if statements involved. I have maticulously gone through the code and discovered an issue with the cards being anchor elements that contain inputs and forms. This wasn't allowed by the validator, so I instead made the anchor an individual element within the card that stretched across the height and width of it. This created an issue with the buttons section, which I decided to separate using border top on the art to cart and book buttons. I also needed to change the p elements within the buttons to span elements instead.

- [about.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/home/templates/home/about.html) returned no errors.

- [index.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/home/templates/home/index.html) returned no errors.

- [checkout.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/checkout/templates/checkout/checkout.html) had an empty h1 tag that was being used for the spinner, I made this a p element and gave it a large font size. There was also a p element within a span, so I changed the span to a div. Lastly there was another p inside a button, so I changed the p element to a span.

- [checkout_success.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/checkout/templates/checkout/checkout_success.html) returned no errors.

- [cart.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/cart/templates/cart/cart.html) returned no errors.

- [mobile-navbar.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/includes/mobile-navbar.html) contained li elements within a div, changing them to divs made no difference to the visuals.

- [mainnavbar.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/includes/mainnavbar.html) returned no errors.

- [toast_error.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/includes/toasts/toast_error.html) returned no errors.

- [toast_info.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/includes/toasts/toast_info.html) returned no errors.

- [toast_success.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/includes/toasts/toast_success.html) returned an error for using a strong element within a p element, removing the p element made no difference to the site visually.

- [toast_warning.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/includes/toasts/toast_warning.html) returned no errors.

#### All Auth HTML Templates

- All auth's [base.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/base.html) returned no errors.

- [already_logged_in.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/snippets/already_logged_in.html) returned no errors.

- [account_incactive.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/account_inactive.html) returned no errors.

- Account's [base.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/base.html) returned no errors.

- [email_confirm.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/email_confirm.html) returned no errors.

- [email.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/email.html) contained a trailing slash and type="text/javascript" on script element which was deemed unneccesary.

- [login.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/login.html) returned no errors.

- [logout.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/logout.html) returned no errors.

- [password_change.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/password_change.html) returned no errors.

- [password_reset_done.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/password_reset_done.html) returned no errors.

- [password_reset_from_key_done.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/password_reset_from_key_done.html) returned no errors.

- [password_reset_from_key.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/password_reset_from_key.html) had a trailing slash.

- [password_reset.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/password_reset.html) had a duplicate attribute of class on an element, and a trailing slash.

- [password_set.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/password_set.html) returned no errors.

- [sifgnup_closed.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/signup_closed.html) returned no errors.

- [signup.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/signup.html) returned no errors.

- [verification_sent.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/verification_sent.html) returned no errors.

- [verified_email_required.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/account/verified_email_required.html) returned no errors.

- [login_extra.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/socialaccount/snippets/login_extra.html) returned no errors.

- [provider_list.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/socialaccount/snippets/provider_list.html) returned an error for the li not being inside a list.

- [authentication_error.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/socialaccount/authentication_error.html) returned no errors.

- Social account's [base.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/socialaccount/base.html) returned no errors.

- [connections.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/socialaccount/connections.html) had a stray end div tag.

- [login_cancelled.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/socialaccount/login_cancelled.html) returned no errors.

- [signup.html](https://github.com/ryanmcnally93/project-four-ascension/blob/main/templates/allauth/socialaccount/signup.html) returned no errors.

#### CSS

I have tested all my CSS with the [W3C Validator.](https://jigsaw.w3.org/css-validator/#validate_by_input)

- [base.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/static/css/base.css) had an error where a colon was missing from a min-width filter, which is now present.

- [rehearse.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/rehearse/static/rehearse/css/rehearse.css) returned no errors.

- [record_studio.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/record_studio/static/record_studio/css/record_studio.css) returned no errors.

- [products.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/static/products/css/products.css) had 'margin: none;' halfway down. This has now been fixed to 'margin: 0;'

- [add_products.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/static/products/css/add_products.css) returned no errors.

- [home.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/home/static/home/css/home.css) returned no errors.

- [about.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/home/static/home/css/about.css) returned no errors.

- [checkout.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/checkout/static/checkout/css/checkout.css) returned no errors.

- [cart.css](https://github.com/ryanmcnally93/project-four-ascension/blob/main/cart/static/cart/css/cart.css) returned no errors.

<p>
  <a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img  style="border:0;width:88px;height:31px;margin:auto;display:flex;"
          src="http://jigsaw.w3.org/css-validator/images/vcss"
          alt="Valid css!" />
    </a>
</p>

### Javascript Validation

I have tested all my JavaScript code using JSHint.

- [base.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/static/js/base.js) returned no errors.

- [base_extra.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/static/js/base_extra.js) returned no errors.

- [products.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/static/products/js/products.js) was missing semicolons in five positions, these are now in position.

- [product_information.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/static/products/js/product_information.js) returned no errors.

- [add_products.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/static/products/js/add_products.js) returned no errors.

- [edit_products.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/products/static/products/js/edit_products.js) had one missing semicolon.

- [cart.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/cart/static/cart/js/cart.js) returned no errors.

- [stripe_elements.js](https://github.com/ryanmcnally93/project-four-ascension/blob/main/checkout/static/checkout/js/stripe_elements.js) returned some missing and uneccesary semicolons.

#### Python Validation

<!-- DJANGO UNIT TESTS -->

#### Pep8 Compliancy

<!-- - To check if all my .py files were pep8 compliant, I used [Code Institutes pep8 linter](https://pep8ci.herokuapp.com/), This returned many issues with the lengths of my Python code lines.

- To solve this I pip installed [Black](https://black.readthedocs.io/en/stable/getting_started.html), running the command "black -l 79 (name of python document)". -->

### Lighthouse

##### Index

<img src="/media/readme-images/index-desktop.png" width="100%" alt="Index lighthouse score on desktop" style="display: inherit; ">

##### Various All Auth Pages

- Login Page

<img src="/media/readme-images/login-desktop.png" width="100%" alt="Login lighthouse score on desktop" style="display: inherit; ">

- Logout Page

<img src="/media/readme-images/logout-desktop.png" width="100%" alt="Logout lighthouse score on desktop" style="display: inherit; ">

- Register Page

<img src="/media/readme-images/register-desktop.png" width="100%" alt="Register lighthouse score on desktop" style="display: inherit; ">

##### About

<img src="/media/readme-images/about-desktop.png" width="100%" alt="About lighthouse score on desktop" style="display: inherit; ">

##### Rehearse

<img src="/media/readme-images/rehearse-main-desktop.png" width="100%" alt="Rehearse lighthouse score on desktop" style="display: inherit; ">

##### Meet the Engineers

<img src="/media/readme-images/engineers-desktop.png" width="100%" alt="Meet the engineers lighthouse score on desktop" style="display: inherit; ">

##### Record

<img src="/media/readme-images/record-main-desktop.png" width="100%" alt="Record page lighthouse score on desktop" style="display: inherit; ">

##### Profile Page

<img src="/media/readme-images/profile-desktop.png" width="100%" alt="Profile page lighthouse score on desktop" style="display: inherit; ">

##### Products Page

<img src="/media/readme-images/products-desktop.png" width="100%" alt="Products lighthouse score on desktop" style="display: inherit; ">

##### Product Information

<img src="/media/readme-images/product-information-desktop.png" width="100%" alt="Product information page lighthouse score on desktop" style="display: inherit; ">

##### Add Product

<img src="/media/readme-images/add-product-desktop.png" width="100%" alt="Add product page lighthouse score on desktop" style="display: inherit; ">

##### Edit Product

<img src="/media/readme-images/edit-product-desktop.png" width="100%" alt="Edit a product page lighthouse score on desktop" style="display: inherit; ">

##### Checkout

<img src="/media/readme-images/checkout-desktop.png" width="100%" alt="Checkout page lighthouse score on desktop" style="display: inherit; ">

##### Checkout Success

<img src="/media/readme-images/checkout-success-desktop.png" width="100%" alt="Checkout success lighthouse score on desktop" style="display: inherit; ">

##### Cart

<img src="/media/readme-images/cart-desktop.png" width="100%" alt="Cart lighthouse score on desktop" style="display: inherit; ">

### Lighthouse Mobile

##### Index

<img src="/media/readme-images/index-mobile.png" width="100%" alt="Index lighthouse score on mobile" style="display: inherit; ">

##### Various All Auth Pages

- Login Page

<img src="/media/readme-images/login-mobile.png" width="100%" alt="Login lighthouse score on mobile" style="display: inherit; ">

- Logout Page

<img src="/media/readme-images/logout-mobile.png" width="100%" alt="Logout lighthouse score on mobile" style="display: inherit; ">

- Register Page

<img src="/media/readme-images/register-mobile.png" width="100%" alt="Register lighthouse score on mobile" style="display: inherit; ">

##### About

<img src="/media/readme-images/about-mobile.png" width="100%" alt="About lighthouse score on mobile" style="display: inherit; ">

##### Rehearse

<img src="/media/readme-images/rehearse-main-mobile.png" width="100%" alt="Rehearse lighthouse score on mobile" style="display: inherit; ">

##### Meet the Engineers

<img src="/media/readme-images/engineers-mobile.png" width="100%" alt="Meet the engineers lighthouse score on mobile" style="display: inherit; ">

##### Record

<img src="/media/readme-images/record-main-mobile.png" width="100%" alt="Record page lighthouse score on mobile" style="display: inherit; ">

##### Profile Page

<img src="/media/readme-images/profile-mobile.png" width="100%" alt="Profile page lighthouse score on mobile" style="display: inherit; ">

##### Products Page

<img src="/media/readme-images/products-mobile.png" width="100%" alt="Products lighthouse score on mobile" style="display: inherit; ">

##### Product Information

<img src="/media/readme-images/product-information-mobile.png" width="100%" alt="Product information page lighthouse score on mobile" style="display: inherit; ">

##### Add Product

<img src="/media/readme-images/add-product-mobile.png" width="100%" alt="Add product page lighthouse score on mobile" style="display: inherit; ">

##### Edit Product

<img src="/media/readme-images/edit-product-mobile.png" width="100%" alt="Edit a product page lighthouse score on mobile" style="display: inherit; ">

##### Checkout

<img src="/media/readme-images/checkout-mobile.png" width="100%" alt="Checkout page lighthouse score on mobile" style="display: inherit; ">

##### Checkout Success

<img src="/media/readme-images/checkout-success-mobile.png" width="100%" alt="Checkout success lighthouse score on mobile" style="display: inherit; ">

##### Cart

<img src="/media/readme-images/cart-mobile.png" width="100%" alt="Cart lighthouse score on mobile" style="display: inherit; ">

## Manual Testing

This project has been tested using the following browsers:

Chrome, Safari & Edge

On the following devices:

Desktop Macbook, Ipad Air Simulator & IPhone 5/SE simulator

### Base

#### Navbar

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Logo | Underlines on hover, reloads page | Hovered over and clicked | White underline added, reloads page | Pass |
| User Options & Cart | Hover underline on all 3 screen sizes | Loaded on IPhone, IPad and desktop, hovered over | White underline added | Pass |
| User Options | Two options, register and login | Click when not logged in | Register and login available only | Pass |
| User Options | Five options, including adding and dditing products | Click when logged in as superuser | All five options available | Pass |
| User Options | Two options, profile and logout | Click when logged in as normal user | Correct two options available | Pass |
| Cart | Takes user to cart page when clicked | Clicked on cart | Taken to cart page | Pass |
| Cart | Price updates when product added | Travelled to products, added item | Item added to cart and price visible | Pass |
| Logo | Views as smaller icon and acts same way on small screens | Loaded on IPhone, hovered and clicked | Small icon, White underline added, reloads page | Pass |
| Five navigation tabs on next bar | Background's and text change colour, clicking shows options | Hovered and clicked on all five options | Colours change, options show | Pass |
| Five non products page links (about, contact, record main, engineers, rehearsal main) | Hovers and links work | Hovered and clicked on all five options | Colours change of background and text, links work | Pass |
| Three Studio links | Products page opens as desired, hover change works | Hovered and clicked on all three options | Colours change of background and text, links work, Studio is header and borders are gold, sort and direction work | Pass |
| Three Rehearsal links | Products page opens as desired, hover change works | Hovered and clicked on all three options | Colours change of background and text, links work, Rehearsal Rooms is header and borders are lightblue, sort and direction work | Pass |
| Strings link | Products page opens as desired, hover change works | Hovered and clicked on strings link | Colours change of background and text, link works, only strings show | Pass |
| Three Shop links | Products page opens as desired, hover change works | Hovered and clicked on all three options | Colours change of background and text, links work, studios and rehearsals not present, sort and direction work | Pass |
| All products link | Products page opens as desired, hover change works | Hovered and clicked on all products | Colours change of background and text, link works, sort and direction work | Pass |
| Sale items link | Products page opens as desired, hover change works | Hovered and clicked on sales item link | Colours change of background and text, link works, only sales items present | Pass |

#### Footer
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| All three socials | White underline adds on hover | Hovered over all three icons | Underline was added on each | Pass |
| Facebook Icon | Takes user to facebook.com | Clicked icon | Took me to facebook.com | Pass |
| Instagram Icon | Takes user to instagram.com | Clicked icon | Took me to instagram.com | Pass |
| Twitter Icon | Takes user to twitter.com | Clicked icon | Took me to twitter.com | Pass |
| Social media icons | Hover and links work on other two sizes | Opened on two dev simulators and hovered and clicked | Underlines added, links correct | Pass |
| Footer | Writing on left disappears, middle text is on left | Opened webpage on smaller device | Information displays ass desired | Pass |

<img src="/media/readme-images/footer-testing.webp" width="100%" alt="The Footer on smaller screens" style="display: inherit; ">

#### Toggler

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Toggler | Only available on Medium and smaller devices | Opened on all three devices | Could only access on IPad and IPhone | Pass |
| Toggler | Hovering CSS change and opens and closes on click  | Hovered over and clicked | Opens and closes, CSS changes text and background colours (I also added Jquery to slide up and down rather than just appear) | Pass |

### Homepage

#### Background

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Background Image | Stays Central when extending image on large screens | Opened on desktop, dragged window wider | Image stayed central, opened up wider and revealed more | Pass |

#### Main Buttons and text div

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Three main buttons | Hover CSS changes and links work | Hovered over buttons and clicked | Colours changed, links work | Pass |
| Text div | Stays central and lifts up on Mobile | View on multiple devices | Is at top op page on mobile, middle for other devices, central on all | Pass |
| Three main buttons | Smaller buttons listed as column on small devices | Open on mobile | Buttons are smaller and in a column | Pass |

#### Little Strings Section

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Little strings Logo | Hover CSS changes and link works | Hover over logo and click | White left and right border is added and link works | Pass |
| Little strings Logo | Hover CSS changes and link works | Hover over logo and click on mobile | White bottom border is added and link works | Pass |

### About Us

#### Background (Same test performed on Record & Rehearsal Pages)

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Background | Keeps relevant height and width on multiple devices | Open page on all devices | More height on large screens, centralised on all, can still make out image on smallest screens | Pass |

<img src="/media/readme-images/about-testing.webp" width="100%" alt="The About Us page on desktop screens" style="display: inherit; ">

#### Header and text div (Same test performed on Record & Rehearsal Pages)

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Header | Stays underneath navbars | Open on multiple devices | Stays at the top of the page | Pass |
| Text Div | Font size smaller on smaller pages, text div stays in center | Opened in dev tools, changed size smaller and larger to watch div move | Stays in center, font-size remains relevant to screen size | Pass |

#### Contact Us Section

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Header | Stays underneath image | Move window wider and smaller on dev tools | Stays in correct position | Pass |
| IFrame | Moves underneath text on smaller devices | Opened on mobile | Correct position | Pass |
| IFrame | Controls all work | click on all clickable links | Google links work, zoom in and out works by mouse and buttons, satelitte view works | Pass |

### Record Main

#### Engineers Button and Artists Section

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Engineers Button | Hover CSS changes and link works | Hover over and click on button | CSS changes, link works | Pass |
| Artists Section | Views as a column on smaller devices | Open on mobile | Displays as column, Lady Sanity box is reverse so it displays the same | Pass |

### Meet The Engineers Page

#### Engineer Information and Buttons

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Images, buttons and text | Centralise on smaller screens, place either left or right on large | Open on multiple devices | CSS changes, exactly how I want | Pass |
| Buttons | Hover CSS changes and link works | Hover over and click on buttons | CSS changes, links work | Pass |

### Rehearsals Main

#### Different Types of Rooms Section

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Room types boxes | View content as a column on smaller screens | Opened on Mobile | All the data was centered in a column | Pass |

### Products page

#### Filter

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Price High to Low Select | Page refrshes, products view from highest price to lowest | Selected option | The page reloaded, with the correct sort and direction | Pass |
| Price Low to High | Page refrshes, products view from lowest price to highest | Selected option | The page reloaded, with the correct sort and direction | Pass |
| Rating Low to High Select | Page refrshes, products view from lowest rating to highest | Selected option | The page reloaded, with the correct sort and direction | Pass |
| Rating High to Low Select | Page refrshes, products view from highest rating to lowest | Selected option | The page reloaded, with the correct sort and direction | Pass |
| All Products Select | Page refrshes, all products view | Selected option | The page reloaded, with all products on | Pass |
| Choose Filter select | Nothing happens | Selected option | Nothing happened | Pass |

#### Cards

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Card | Whole card acts as an anchor and takes user to product-information | Hover and click | Cursor is pointer, clicking within the card takes user to product-information page for that item | Pass |
| Text and Button | Both have hover qualities | Hover | The text changes colour and underlines, the button has the bg-darkblue class which changes to white | Pass |
| Button | Clicking add to cart adds to the quantity and places item in cart | Click on add to cart | Item is added to cart, button changes to quantity box | Pass |
| Quantity Box | Clicking increase adds another of the same item | Click on plus symbol | Another of the same item is in the cart | Pass |
| Quantity Box | Decrease button works too | Click on minus button | Takes one of that item out of the cart, if last item, deletes the item from cart and original button is back | Pass |
| Page reload | Clicking on the various card buttons reloads the aage, but directs user back to item they were just looking at | Click add to cart on several items | Kept returning back to that product | Pass |
| Hire Room button | Takes user to product-information | Click book | Takes user to product-information for that item | Pass |

<img src="/media/readme-images/product-testing.webp" width="100%" alt="The Product page on desktop screens" style="display: inherit; ">

### Product Information page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Layout | Information lists in a column on small screens | Open on mobile | All the product information is listed within a single column | Pass |
| Edit Button | Takes user to Edit product page with this products infommation inserted, hover CSS change on text | Hover and click on edit | Underlines text, takes user to edit a product, information is pre-populated for that item | Pass |
| Delete Button | Opens a modal making sure the user is aware of this decision, hover CSS changes | Hover and click on Delete | Text is underlined, opens up modal | Pass |
| Edit Button | Unregistered users cannot open page | Click on button | Clicked on button, received error on toast | Pass |
| Delete Button | Doesn't allow users who aren't superusers to open the modal to delete | Click delete | Opened up the modal | FAIL |

- This will have to be rectified.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Back to Products button | Takes user back to products, hover CSS changes | Hover and click on back to products | Colours change and link takes user back to products | Pass |
| Add to cart Button | Clicking add to cart adds to the quantity and places item in cart, hover CSS change | Hover and click on add to cart | Hover works, item is added to cart, button changes to quantity box | Pass |
| Quantity Box | Clicking increase adds another of the same item | Click on plus symbol | Another of the same item is in the cart | Pass |
| Quantity Box | Decrease button works too | Click on minus button | Takes one of that item out of the cart, if last item, deletes the item from cart and original button is back | Pass |

#### Hire Rooms

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Different elements for Hire Rooms | Includes equipment provided, datepicker and text asking user to pick date | Open page for hire room | Relevant elements available | Pass |
| Equipment Provided | Hover CSS changes, takes user to rehearsal page with product equipment information | Hover and click on button | Takes user to desired location, hover CSS changes | Pass |
| Datepicker | Choosing a date returns the times available for that date | Click on a date | Five time slots become available, from 10am to 3pm | Pass |
| Datepicker | Cannot choose past date | Click on past date, enter time and click add to cart | Error message displayed in toasts | Pass |
| Datepicker | Cannot pick date more than two weeks into future | Click on date too far into future | Error message displayed in toasts | Pass |
| Timepicker | Clicking on one radio takes focus off another | Click on a sequence of radio buttons | Each one removes the focus from the last | Pass |
| Both Datepicker and Timepicker | Cannot POST form without picking both a date and a time | Attempted to add to cart without date first, then with date but without time | Error message displayed in toasts on both occasions | Pass |
| Add to Cart | Hover CSS changes, adds session to cart | Pick date and time, hover over button and click | Hover CSS changes, session added to cart | Pass |

### Add a Product Page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Category Dropdown | Lists all categories | Click on dropdown | All categories displayed | Pass |
| SKU, name, description and price | Form cannot be submitted by omitting one of these items | Attempted to POST form without each of these items individually | None of them POSTed | Pass |
| Price limit of characters | Cannot add more than six digits to price | Typed 957738 into price and submitted form | Form did not POST, error message provided | Pass |
| Striked Price | Makes item an offers item | Added Striked price when adding product | Item did not list in sales items |FAIL |

- I added some JavaScript to the is_offers_item field which is invisible to make the item list as an offers item. This test now passes.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Hire Room Dropdown | Contains Yes and No options | Clicked |  | Pass |
| Hire Room Dropdown | Makes product a hire room | Added product as a hire room, viewed product-information page | Page displays as a hire room | Pass |
| Image uploaders | Hover CSS changes, opens up an image uploader box, clicking on an image reveals the name on the webpage so you know which item you are uploading | Hovered over and clicked on image button, selected image and clicked open | Image name was visible on page | Pass |
| Giving no image | Creates product with default no-media image | Added product without image | Was redirected to product-information, product had default no-media image | Pass |
| Images | Not available on mobile devices | Opened page on mobile | Images were not visible | Pass |
| Form | Should not POST without Name | Attempt to fill in other fields and POST | Input warning shown, did not POST | Pass |
| Form | Should not POST without Decsription | Attempt to fill in other fields and POST | Input warning shown, did not POST | Pass |
| Form | Should not POST without SKU | Attempt to fill in other fields and POST | Input warning shown, did not POST | Pass |
| Form | Should not POST without Price | Attempt to fill in other fields and POST | Input warning shown, did not POST | Pass |
| Form | Shouldn't be able to add antyhing other than text and numbers in field | Added pattern in forms.py, attempting to add '//' in field and POST | Did not accept | Pass |
| Form | Shouldn't be able to POST with just spaces | Added pattern in forms.py, attempting to add four spaces in field and POST | Did not accept | Pass |
| Form | Shouldn't be able to POST with less than 4 characters | Added minlength in forms.py, attempting to add three characters in fields and POST | Did not accept | Pass |
| Form | Two price fields should no  accept anything other than numbers with a potential decimal | Attempted to add other letters, also attempted three digits after decimal | Could not enter anything other than numbers and one decimal, three digit input gave error and didn't POST | Pass |
| Form | Changing category should change the is hire room | Made is hire room display and changed category to studio room and back, then rehearsals and back | JavaScript manages to update the input box correctly | Pass |

- These same form tests were completed on the Edit a Product page.

### Edit a Product page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Edit a product form | Should react the same way as the add a product form | Tested all tests previously mentioned in add a product form | All tests passed | Pass |
| Searchbar | Cannot find an item if none is selected | Searched for 'pick an item' | Error message shows | Pass |
| Searchbar | Clicking on any item reveals that items current settings | Clicked on first guitar strings product | The form filled with the data of that product | Pass |

### Cart page

#### Empty

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Whole Page | Gives relevant message when cart is empty | Clicked onto page with empty cart | Message displayed | Pass |

#### Buttons

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Remove all button | Hover CSS changes and removes all of that item | Hovered and clicked on remove all | All of that item removed | Pass |
| Quantity Add | Button is disabled if it is on a session item, ad they need a date and time added | Hovered over the quantity add button, attempted to click | No hover qualities, click did not work | Pass |
| Quantity Add | Able to add an item that is not session | Click on quantity plus on regular product | Item is added to cart | Pass |
| Quantity Minus | Takes item from cart, including sessions | Hover and click on quantity minus | Hover CSS changes, product is taken from cart, if same date but different time, last time added is taken away | Pass |
| Empty Cart | Opens modal | Hover and click on empty cart | Hover CSS changes, modal opens | Pass |
| Back to Products | Hover CSS changes and takes user back to products | Hovered and clicked on back to products | Hover CSS changes, user taken back to products | Pass |
| Secure Payment | Hover CSS changes and takes user to checkout page | Hovered and clicked on Secure Payment | Hover CSS changes, taken to checkout page | Pass |

<img src="/media/readme-images/cart-testing.webp" width="100%" alt="The Cart page on desktop screens" style="display: inherit; ">

#### Products

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Same Date Sessions | Quantity for that date increases, quantity for that overall item on products page increases, time added to string on the cart item | Added two times with the same date and product | All desired outcomes met | Pass |
| Different Date, Same Item | Two instances of same item in cart | Added same product, different date | Two items in cart, quantity of item on products page equals two though | Pass |
| Products | Display as a column on small screens | Opened site on mobile | The items are all centrally aligned | Pass |
| Product image and name | Cursor changes to pointer, takes user to relevant product-information page | Hovered and clicked on image, then on name | The links work and the cursor changes | Pass |

### Checkout page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Whole page | Unregistered user is unable to load the page | logged out and attempted to secure payment | Taken back to login page | Pass |
| Save info radio button | Information should save to profile page | Click button, fill in form | Billing information saves to profile. | Pass |
| Payment | test card data sends through fake payment | Added fake dard details '4242 4242 4242 4242' to the card information and proceeded with payment | Payment went through | Pass |
| Two buttons | Hover CSS changes and buttons work | Hover and click on both buttons | CSS changes for both, user taken to cart on first, and payment info sent on second | Pass |
| Products and form | Display in a single column on smaller devices | Open page on mobile | Products first, the form underneath, all in a column | Pass |
| Form | Only numbers should be able to be in phone_number field | Attempted to type letters and symbols into phone_number input | Could not type anything other than numbers | Pass |
| Form | Email field should only accept valid emails | Attempted to POST with words and no @ symbol | Could not POST with incorrect format | Pass |
| Form | Phone number should not accept any input that isn't 11 characters long | Attempted 10 and 12 characters | Could not POST | Pass |
| Form | Should not be able to POST without required information | Attempted to send form without each required field set | Form wouldn't POST | Pass |
| Form | Should not be able to POST with symbols in fields | Attempted to sdd // and "" from field to field | Form wouldn't POST | Pass |
| Form | Should not accept (in fields that aren't phone number and email) less than 4 characters | Attempted to add 3 characters to relevant fields | Form wouldn't POST | Pass |
| Form | Should not be able to enter just spaces | Type 4 spaces into full name field and POST | Error message displays| Pass |

### Checkout Success page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Order number | Visible within text div | Checkout | Order number available in text div | Pass |
| Hire Room line items | Display separate items for different dates | Add two sessions with different dates but same product and checkout | Two line items created, font-size smaller and break added to make look better | Pass |
| Back to products button | Hover CSS changes and link takes user to products page | Hover and click on button | CSS changes, link works | Pass |

### Profile page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Update information | Changing data and clicking button changes data permanently | Changed name and clicked button | Data updates | Pass |
| Two buttons at bottom of form | Both have hover qualities, connected accounts takes user to correct page | Hovered over two buttons, clicked on connected accounts | Hover CSS changes, link works | Pass |
| All data | Displays as a column on smaller screens | Opened on mobile | Displays as column | Pass |
| Order Number links | Underline should be added, links to old checkout success page | Hover and click on link | Hover and link works | Pass |
| Form | Should not save symbols in fields | Attempted to type '//' and '**' and save | Would not save information | Pass |
| Form | Should not be able to set phone number to character length that isn't 11 | Attempted 10 and 12 characters | Would not save information | Pass |
| Form | Should not be able to type anything other than numbers into phone number field | Attempt letters | Could not type anything other than numbers | Pass |
| Form | Should not be able to save if fields are less than 4 characters long | Type eee and hit save | Would not save information | Pass |
| Form | Should not be able to enter just spaces | Type 4 spaces into full name field and POST | Error message displays| Pass |

### Toast Messages

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Success template | When on profile page, images cart products do not show | Perform successful login with items in cart | Items not shown | Pass |
| Success template | Items in cart shown when adding them to cart and changing quantities | Click add to cart twice on a product | Success message contains relevant images and quantities | Pass |
| Information template | Displays with different colour and icon | Click on previous order number from profile page | Previous order shown, and information box is blue with 'i' icon for information | Pass |
| Warning template | Test should reveal correct colour and warning icon | Changed messages.info to messages.warning and triggered | Colour is yellow and warning icon shows, can use when needed | Pass |
| Error template | Check colour and icon | Add incorrect date into datepicker, don't add time and add to cart | Colour is red, icon is 'x' | Pass |

### Modals
Both modals tested

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Delete button | If not superuser, should return error message | Not logged in, type URL for delete product | Messages error shown, delete not completed | Pass |
| Delete button | Removes product from list of products | As superuser, click delete product on modal | Test product deleted | Pass |
| Both buttons | Hover qualities work, cancel button closes modal | Hover over two buttons, click cancel | Hover CSS changes, modal closes | Pass |
| Close buttons | Both modals can be closed using close button | Open both modals and click 'x' in corner |  | Pass |

### Various All Auth Pages

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Login page | User should login | Type in superuser credentials | User logged in | Pass |
| Logout page | Both buttons have CSS qualities and links work | Hover and click on both buttons | No takes user to index, yes logs out user and also directs to index | Pass |
| Register page | Adds test user | Type testytest@test.com, username testytest, password = testpassword | Sends email successfully | Pass |
| Register page | Displays as column on smaller screens | Test page on mobile screens | Page displays in column | Pass |
| Register Form | Will not accept spaces in username | Put name with space in between and POST | Did not accept, displayed error message | Pass |
| Register page | Should not accept symbols in username | Tried to add '//' | Did not accept | Pass |

This readme.md will be spellchecked using the spell checker extension for Chrome.