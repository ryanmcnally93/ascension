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
|  |  |  |  | Pass |

### Products page

### Product Information page

### Add a Product Page

### Edit a Product page

### Cart page

### Checkout page

### Checkout Success page

### Toast Messages

### Modals

### All Auth???

This readme.md will be spellchecked using the spell checker extension for Chrome.