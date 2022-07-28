# DJ Flamingo Gig Manager

Flaming manager is a web application that was developed to be a useful tool for small artists and producers of the night life business. The application is currently set to handle a singe agency/producer and its artists, but with a possible extension in the future. There are two types of users, one is the admin or the super-user, that is the agency producer that is responsible for arrange the events from the venues and set to one of the DJs using the application. The admin also can set the event as confirmed or as a proposal waiting for the confirmation from the designed DJ. The other type of user is the DJ, that can access the information of all its events, accept and refuse it as well. The events are displayed on the DJ main page in order from the sooner to later.

# Technology Used
### Languages
- **Python**
- **HTML**
- **CSS**
- **JQuery/JavaScript**

### Framewors and Libraries
- **Django**
- **Bootstrap**
- **Cloudinary**

### Database Managment
- **PostgreSQL**
- **Gunicorn**

### Deploiment
- **Heroku**

### Development Enviroment and Git
- **GitPod**
- **GitHub**

### Documentation

- **Wireframecc**
For pre design. Link to their website: [Wireframecc](https://wireframe.cc/)
- **LucidCharts**
Used to make the flowchart. Link to their website: [LucidChart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=354596043016&km_CPC_TargetID=aud-536921399221:kwd-33511936169&km_CPC_Country=1010751&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjw54iXBhCXARIsADWpsG9JQtgJHpOUTSj1i_7k4312Yu47bI5qlULv-9jo5deTjR4dl7270j8aAgAfEALw_wcB)
- **Microsoft Excel**
For database tables vizualizations
- **Microsoft Paint**
For images and captures

# Site Goals

fill with some text

# UX

## Responsiveness

- **Views**
<details>
<summary>View Mobile View</summary>

![View Mobile View](/docs/images/flamingoMobileResponsive.png)
</details>

## User Stories
### Admin
- As an **admin** I can **create, edit, and delete** gigs so that I can **update the gigs for the DJ**
- As an **admin** I can **delete a selected user** so that the user data **will be deleted from database**
- As an **admin** I can **set the agency tax** for each gig so that even if the tax changes in the future old gigs the old tax will remain
- As an **admin** I can click to **see all the user** registered so that see a table with all users
- As an **admin** I can **click in on gig to view** so that access **more info about it**
- As an **admin** I can use a f**ilter bar on the admin/home** so that **select the data** that I want to be displayed on the table
- As an **admin** I can **access the history** of the gigs so that I’ll have **stored data** from gigs

### User DJ Stories
- As a **DJ/use**r I can accept or refuse a gig offer so that I can let the admin know my answer about a proposal
- As a **DJ/user** I can **click in on gig** to view so that **access more info about it**
- As a **DJ user** I can **view my own gigs** by order of date so that I have a **general vision about my next gigs**
- As a **DJ/user** I can **expect that the fees are calculated** so that know exactly how much I **should receive**
- As a **DJ/user** I can **get a specific view if I don't have any gigs assigned** so that know about my current gigs situation
- As a **user** I can **registrate or login** so that view **my page of gigs**

# Development Planes

## Strategy

The electronic music has conquered the world, the scene took the lead of the night life and DJ sets became a common thing, from small dance clubs to big international festivals. Naturally the producers and agencies behind those events grew as well and the electronic music was consolidated as crucial part of the entertainment business. However fresh new musicians and artists struggle to find a stage with good payment deal. At the most cases the music gigs are not the primary income for artists, so looking for gigs and managing them takes a long and precious time. Flaming manager is addressed to those small artists and producers that does not have time or the structure that big agencies and musicians have to manage their events.

### Target

**Amateur or beginning DJs.**

The aim of the software is to provide to the DJ simple information about when, where, and how much I’ll make of each gig

**Music and event producer.**

For the admin is to provide tools to create and assign gigs for the musician, keep an overall view of the gigs and edit it if necessary





## Scope

The scope of the software should cover all the features that will achieve functionalities discussed on the strategy and the objective of the product.

- **Require Features**
    -  Only admins can create, delete, and edit gigs and venues
    -  Display for each user its own gigs
    -  Gigs can be created as a proposal or confirmed
    -  Users can accept or refuse a gig proposal
    -  Gigs are displayed in order of date
    -  Only display gigs with dates in future
    -  Show history of past gigs

- **Desired Features**
    - Each gig shows how many days is due to
    - Agency fees can be assigned differently for each gig

## Skeleton

Initially a wireframe was created to set the main layout for the software. The header and footer features are fixed, and the content is dynamic changing depending on the user action and attributes. However I didn’t create wireframes for the other pages since that the main layout were already chosen.

- ### User Agenda

Home page where the user's gig are displayed by order and in cards
<details>
<summary>View ser/DJ Agenda Home</summary>

![View Agenda User Home](/docs/images/app_design_home.png)
</details>
<br/>

- ### Gig Details

Details page that contains the main info and actions
<details>
<summary>View Gig Details</summary>

![View Gig Details](/docs/images/app_design_home%20(2).png)
</details>
<br/>

## Structure
The project Flamingo is composed of two apps responsible for different functionality of the website.

- **Agenda App**

Responsible for the gigs management engine, has the models for gigs and venues and the views are responsible for displaying information about the gigs and post actions to update them

- **Acounts App**

App that holds the functionality of the managing the user’s authentication and registration. It holds the custom model for the user, the views are responsible for the login, registration, and logout.

**Flowchart**
<br/>
<details>
<summary>View App Flowchart</summary>

![View App Flowchart](/docs/images/flowchart.png)
</details>
<br/>

**Data Structure**
<br/>
<details>
<summary>View Data Structure</summary>

![View Data Structure](/docs/images/dataStructure.png)
</details>
<br/>

## Surface

**Colors**

- Palette of colors

![Colors](/docs/images/colours_pallet.png)


**Font**

- The project uses **Poppins** from google fonts as the first choice, and sans-serif.

**Images**

- The flamingo on the logo was taken from: [freepng](https://www.freepng.es/)
- The flamingo with sunglasses was taken from: [dreamstime](https://www.dreamstime.com)
- The landing picture was taken from: [Pexels](https://www.pexels.com/)

# Features

## Fixed Features

- **Landing Page**

    - Displayed as standard page for the application when the user is not registered or logged out.

<br/>
<details>
<summary>View Landing Page</summary>

![View Landing Page](/docs/images/flamingLanding.png)
</details>
<br/>

- **Navigation Bar(Header)**
    
    - Appears in every page of the application to facilitate the user navigation thru the website
    - A Home link that brings directly to the main page of the user
    - Login link to a login form 
    - Register link to a registration form for new users
    - The name “Flamingo” is also a link that redirect to main page
    - When the user is logged in a word “Welcome” and the username is displayed
    - Also, when the user is logged in, the “Logout” appears that will logout the user and redirect to the landing page

<br/>
<details>
<summary>View Header</summary>

![View Naigation Bar](/docs/images/flamingoHeader.png)
</details>
<br/>

- **Foot bar**

    - Information of the developer and social media links

<br/>
<details>
<summary>View Footer</summary>

![View Footer](/docs/images/flamingFooter.png)
</details>
<br/>

## Dynamic Features

This section is designed to contain all the main information and tools of the application, the components inside will dynamically change as the user navigate on the website.

### Admin Features

#### Main Page

- **Menu Buttons**
    - Create a Gig link to the page with a form for the creation of a new gig
    - Create a venue link to the page with a form to the creation of a new venue
    - My DJs, a link for a page with information of all the registered DJs
    - Past gigs, a link for a page with information of all the gigs that the date is already past

- **Filter Bar**
    - A section with filter that can be applied to the table, the gigs can be filtered by the DJ, venue and in a period of time
    
- **Table of Gigs**
    - Table where is displayed all the programmed gigs, with some basic information and a button to bring to a more detailed vision of the gig.

<br/>
<details>
<summary>View Admin Page</summary>

![View Admin Page](/docs/images/flamingoAdminAgenda.png)
</details>
<br/>

#### Create Gig

- Is the page that contains the form to create a gig. The form has a few placeholders to make it easy to understand the fields and also some fields with specific datatypes are arranged to facilitate the usage. By the end of the form a button “Create” will validate the gig and redirect the user to the main page. Due to the database design each gig has to have a name and unique, only the field “info” can be set as empty. Any problems with the validation the website will display an error message and redirect to the form keeping the previous entered data to correction

<br/>
<details>
<summary>View Create Gig</summary>

![View Create Gig](/docs/images/flamingoCreateGig.png)
</details>
<br/>

#### Create Venue

- Display a page with a form to the creation of a new venue. All the fields are string and the only ones that can be let blank are the “website” and “info”.

<br/>
<details>
<summary>View Create Venue</summary>

![View Create Venue](/docs/images/flamingoCreateVenue.png)
</details>
<br/>

#### My Djs

- Display a table with information about each user/DJ that is registered on the application. A button “View Details” is displayed in each row of the table that brings the user to a more completed view of a specific DJ

<br/>
<details>
<summary>View My Djs</summary>

![View My Djs](/docs/images/flamingoUsersList.png)
</details>
<br/>

#### Mange DJ Account

- Page that displays information about a specific user, and with a button “Delete User” that will trigger a modal window asking if the user is sure about deleting action

#### Gigs History

- At this page a table is displayed where each row holds information about the gig that was already taken place.

<br/>
<details>
<summary>View Gigs History</summary>

![View Gigs History](/docs/images/flamingoAdminHistory.png)
</details>
<br/>

#### Gig Details

- This page display more completed information about a selected gig. The page uses the same template as the DJ view but in the case of the admin there is a button “Edit Gig” where direct the user to a form to edit that gig.

<br/>
<details>
<summary>View Gigs Details</summary>

![View Gigs Details](/docs/images/flamingoGigDetail.png)
</details>
<br/>

#### Update Gig

- This page uses a similar template to the creation of the gig but loads the information of the gig to be edited, after the alteration the user may click on the Update button to post the changes to the database. On the top there is a “Delete” button that will trigger a modal that alert the user that the gig will be deleted from the database.

### User/Dj Featrues

The main page for the DJ user is a agenda like view where the gigs are displayed on cards, ordered by date and holding a few crucial information and actions for that gig.

#### My gigs agenda

- My gigs agenda
Main page for the DJ user, if the user logged in has gigs assigned to happened, they will be displayed in cards with different colours depending on the status of the gig (Confirmed, Proposal or Cancelled). Each card holds a button “Details” that will redirect the user to a page with more information and other actions related to the gig. At the top a button “History” will display the history of gigs of the user.


#### Gigs Cards

- The colour of each card represents their status, being green for confirmed, that means that the admin created already like that or was already accepted by the DJ, light blue is for a proposal, where the admin is proposing a gig for that DJ that can be accepted or declined, red is displayed on the cancelled gig, that was for some reason cancelled by the admin only. Rejected gigs are not displayed for the DJ user.

<br/>
<details>
<summary>View User's Agenda</summary>

![View User's Agenda](/docs/images/flanigoUserAgenda.png)
</details>
<br/>

#### My gigs history

- This page displays a table with the gigs that the date is already in the past. This page is only for a quick view on the gigs history and is paginated for better user experience.


<br/>
<details>
<summary>View User's History</summary>

![View User's History](/docs/images/flamingoUserHistory.png)
</details>
<br/>

#### Gigs Details

- This page displays the more completed information about a selected gig and the venue where is happening, also in the case of being a proposal the buttons “Accept” or “Reject” are displayed, so the DJ can let the admin know the user accepted the gig.

**place img here**

# Testing

- Two approaches were taking during the test routines, one is a manual testing with the direct use of the features and expecting right outcomes, other was made using **unittest** package and **coverage**.

## Manual Test Routine

![Manual Test](/docs/images/flamingoManualTest.png)

<br/>

## Unittest Coverage

### Agenda App Coverage
<br/>
<details>
<summary>View Agenda Coverage</summary>

![agenda coverage](/docs/images/agenda_unittest.png)
</details>
<br/>


### Accounts App Coverage
<br/>
<details>
<summary>View Accounts Coverage</summary>

![accounts coreage](/docs/images/unittest_accounts.png)
</details>
<br/>

### Code Validator Testing

<br/>
<details>
<summary>View Code Validator Table</summary>

![code validator](/docs/images/codeValidators.png)
</details>
<br/>

# Bugs

At the moment the application no major bug is known or still not fixed.

## Fixed Detected Bugs

### Admin can delete other admins accounts.

- A possible dangerous bug was undetected, an admin could delete its own account leading to a very unexpected behaviour of the application. After identifying the possible bug, changes on the logic were made to fix this behaviour.

### Forms not authenticating.

- During the development a major bug occurred where the forms where not able to authenticate it user input. After some research and googling was noticed that the line “{csrf_token}”. After adding the command, the bug was fixed.

### No protected endpoint

- A security branch was detected when any person could just paste the endpoints of the url and would access admin or any user features without authentication. The problem was addressed and all the endpoints for user accounts and admin are protected.

### Styling bugs

- Due to a change in the font family during the development, some html elements needed to update and change the style, in order to keep the layout of the application

## Detected and not fixed bugs

Some minors styling bugs were detected however their occurrence does not interfere with the user experience

### Admin list of gigs styling bug

- At the main page of the admin user on the table that display all the gigs some of the list items have the border a little bit thicker than the others, making a slightly difference between rolls on the table.

# Deployment

This project is deployed on Heroku using the Code Institute's mock terminal

## Heroku

The site is hosted using Heroku, deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.

**To complete a heroku deployment you must follow the steps:**

- Go to the Heroku's website.
- Create an account if required or select log in.
- From the Heroku dashboard, click on the “New” button in top righthand corner then "Create new app".
- Enter a unique "App name" and "Choose a region" before clicking on "Create app".
- Go to "Config Vars" under the "Settings" tab.
- Click on "Reveals Config Vars" and enter the following information:
    - CLOUDINARY_URL : add your cloudinary key here.
    - DATABASE_URL : add the url from postgres database.
    - SECRET_KEY = a secret key for your app.
    - PORT : 8000
- DISABLE_COLLECTSTATIC = 1 during development (Remove when deploying production!)
- Go to "Buildpacks" section and click "Add buildpack".
- Select "/herokupython" and click "Save changes"

## Forking the Project

- Login to GitHub.
- Locate your desired repository.
- Locate the fork option in the top-right hand corner of the repository page.
- You will be asked where you want to fork it to.

## Credits

