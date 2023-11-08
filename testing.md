# Ascension Testing

I have tested my web application automatically and manually using Test Driven Development and Behaviour Driven Development.

## Automated Testing

### W3C Validation

#### HTML

All the following HTML documents (which are written using Django templates), have been validated using the [W3C Validator.](https://validator.w3.org/nu/#textarea)

##### Base

- <!--Errors?-->

##### Index

- <!--Errors?-->

##### Various All Auth Pages

- <!--Errors?-->

##### About

- <!--Errors?-->

##### Rehearse

- <!--Errors?-->

##### Meet the Engineers

- <!--Errors?-->

##### Record

- <!--Errors?-->

##### Profile Page

- <!--Errors?-->

##### Products Page

- <!--Errors?-->

##### Product Information

- <!--Errors?-->

##### Add Product

- <!--Errors?-->

##### Edit Product

- <!--Errors?-->

##### Checkout

- <!--Errors?-->

##### Checkout Success

- <!--Errors?-->

##### Cart

- <!--Errors?-->

#### CSS

The [W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) came back with - <!--Errors?-->

<!-- <p>
  <a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img  style="border:0;width:88px;height:31px;margin:auto;display:flex;"
          src="http://jigsaw.w3.org/css-validator/images/vcss"
          alt="Valid css!" />
    </a>
</p> -->

### Javascript Validation

I have tested all my JavaScript code using JSHint

#### JSHint

<!-- - The main [script.js](/torquay_sunday_league/static/js/script.js) file returned 9 warnings that were letting me know that "const" and "let" are available in ES6. No other errors were found. -->

#### Python Validation

<!-- DJANGO UNIT TESTS -->

#### Pep8 Compliancy

<!-- - To check if all my .py files were pep8 compliant, I used [Code Institutes pep8 linter](https://pep8ci.herokuapp.com/), This returned many issues with the lengths of my Python code lines.

- To solve this I pip installed [Black](https://black.readthedocs.io/en/stable/getting_started.html), running the command "black -l 79 (name of python document)". -->

### Lighthouse

- <!-- ISSUES? -->

##### Base

- <!--Errors?-->

##### Index

- <!--Errors?-->

##### Various All Auth Pages

- <!--Errors?-->

##### About

- <!--Errors?-->

##### Rehearse

- <!--Errors?-->

##### Meet the Engineers

- <!--Errors?-->

##### Record

- <!--Errors?-->

##### Profile Page

- <!--Errors?-->

##### Products Page

- <!--Errors?-->

##### Product Information

- <!--Errors?-->

##### Add Product

- <!--Errors?-->

##### Edit Product

- <!--Errors?-->

##### Checkout

- <!--Errors?-->

##### Checkout Success

- <!--Errors?-->

##### Cart

- <!--Errors?-->

### Lighthouse Mobile

##### Base

- <!--Errors?-->

##### Index

- <!--Errors?-->

##### Various All Auth Pages

- <!--Errors?-->

##### About

- <!--Errors?-->

##### Rehearse

- <!--Errors?-->

##### Meet the Engineers

- <!--Errors?-->

##### Record

- <!--Errors?-->

##### Profile Page

- <!--Errors?-->

##### Products Page

- <!--Errors?-->

##### Product Information

- <!--Errors?-->

##### Add Product

- <!--Errors?-->

##### Edit Product

- <!--Errors?-->

##### Checkout

- <!--Errors?-->

##### Checkout Success

- <!--Errors?-->

##### Cart

- <!--Errors?-->

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

### Checkout Success page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
| Order number | Visible within text div | Checkout | Order number available in text div | Pass |

### Profile page

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
|  |  |  |  | Pass |

### Toast Messages

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
|  |  |  |  | Pass |

### Modals

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
|  |  |  |  | Pass |

### Various All Auth Pages

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --------------------------------------- | ------------------------------------------------------ | ------------------------------------ | --------------------------------------------------- | --------- |
|  |  |  |  | Pass |

This readme.md will be spellchecked using the spell checker extension for Chrome.