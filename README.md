# DJ Flamingo Gig Manager

Flamingo manager is a web application that was developed to be an useful tool for small artists and producers of the night life business. Currently, the application is set to handle a single agency/producer and its artists, with a possible extension in the future. There are two types of users: one is the admin (the super-user), who is the agency producer, responsible for arranging the events and picking one of the Dj's using the application. Additionally, admin can set the event to be confirmed or as a proposal, waiting for the designated Dj’s confirmation. The other type of user is the DJ, who can access the information about all of their events in addition to accepting and refusing the gigs. The events are displayed on the DJ main page chronologically.

## Link to the live application [**Flamingo Gig Manager**](https://flamingodj.herokuapp.com/)

# Table of Content

1 [**Technology Used**](#technology-used)

2 [**Usage**](#usage)

3 [**UX**](#ux)
   * 3.1 [**User Stories**](#user-stories)
   * 3.2 [**User DJ Stories**](#user-dj-stories)

4 [**Development Planes**](#development-planes)
   * 4.1 [**Strategy**](#strategy)
   * 4.2 [**Scope**](#scope)
   * 4.3 [**Skeleton**](#skeleton)
   * 4.4 [**Structure**](#structure)
   * 4.5 [**Surface**](#surface)

5 [**Features**](#features)
   * 5.1 [**Fixed Features**](#fixed-features)
   * 5.2 [**Dynamic Features**](#dynamic-features)
       * 5.3 [**Admin Features**](#admin-features)
       * 5.4 [**User as Dj Features**](#user-as-dj-features)

6 [**Testing**](#testing)
  * 6.1 [**Manual Test Routine**](#manual-test-routine)
  * 6.2 [**Unittest Coverage**](#unittest-coverage)

7 [**Bugs**](#bugs)
  *  7.1 [**Fixed Detected Bugs**](#fixed-detected-bugs)
  *  7.2 [**Detected and not fixed bugs**](#detected-and-not-fixed-bugs)

6 [**Deployment**](#deployment)

7 [**Out of Scope User Stories**](#out-of-scope-user-stories)

8 [**Credits**](#credits)

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

# Usage

As an admin, the user can login with the email and a password. The application will redirect to the main page of an admin, with all the gigs displayed on a table, a menu with options to create gigs, venues and see all the DJ’s and a History of gigs.  The admin can create a gig by filling up a form, assign it to a DJ, select the percentage for the producer’s fees. At the same way venues may be created to hold information about it. So, when create a gig the producer by setting the venue where the event will happen. The details of the gig will also make the venue information available for the users.

After the gig is created it will be displayed at the main page of the admin along with the others, a filter feature is present so in case of high number of gigs on the table the admin can easily filter by, DJ, venue, and dates to find the desired information.

To update or delete a gig the admin can access the button “view details” at the table of gigs and application will display a page with some more details about the selected gig. There the admin can click on update that will display a form to update or a button to delete the gig.

As a DJ the user can login with the email and password to go to the main page. There is displayed the in a form of cards the user’s gigs. Above the gigs cards the are a menu button that brings to the history of gigs made by the user DJ.  The gig cards hold some basic information about the gig and a button access the details view. At the details view the DJ have more information about the event and the venue. In the case of the gig being a proposal made by the admin the user can accept or refuse it by pressing buttons at the bottom of the view.

[**Back to Top**](#table-of-content)

# UX

## Responsiveness

- **Views**
<details>
<summary>View Mobile View</summary>

![View Mobile View](/docs/images/flamingoMobileResponsive.png)
</details>

## User Stories
### Admin
- As an **admin** I can **create, edit, and delete gigs** so that I could **update the gigs for the DJ**
- As an **admin** I can **delete** a selected DJ so I can **update my team**
- As an **admin** I can **set the agency tax** for each gig
- As an **admin** I can click to **see all the user** registered to see a table with all users
- As an **admin** I can **click in on gig to view** to access **more info about it**
- As an **admin** I can use a **filter bar on the admin/home** to **select the data** which I want to be displayed on the table
- As an **admin** I can **access the history** of the gigs so that I’ll have **stored data** from gigs

### User DJ Stories
- As a **DJ/user** I can accept or refuse a gig offer to let the admin know my choice about a proposal
- As a **DJ/user** I can **click in on gig** to view so that **access more info about it**
- As a **DJ user** I can **view my own gigs** chronologically so that I have a **general vision about my next gigs**
- As a **DJ/user** I can **expect that the fees are calculated** to know exactly how much I **should receive**
- As a **DJ/user** I can **get a specific view if I don't have any gigs assigned** to know about my current gigs situation
- As a **user** I can **registrate or login** to view **my page of gigs**

[**Back to Top**](#table-of-content)

# Development Planes

## Strategy

Electronic music has conquered the world, taking the lead of the night life and DJ sets have become a common thing, found both in clubbing and international festivals. Naturally, as the genre boomed, simultaneously the events, the producers, artists and their agencies grew too, escalating in the electronic music being consolidated as a crucial part of the entertainment business. However, upcoming and new artists struggle to find a stage that comes with a fair cost management scheme. Often, the music gigs are not the primary income of artists, thus looking for gigs and managing them takes precious time that they’re lacking. Flamingo manager is addressed to those small artists and producers who simply do not have time or structure to manage their events as well as the giants do.

### Target

**Amateur or beginning DJ's.**

The aim of the software is to provide DJ's some simple information about when, where, and how much can be made at each gig.

**Music and event producer.**

The admin is provided with tools to create and assign gigs for the musician, keep an overall view of the gigs and edit, if necessary.




## Scope

The scope of the software should cover all of the features which achieve functionalities discussed on the strategy and the objective of the product.

- **Required Features**
    -  Only admins can create, delete, and edit gigs, and venues
    -  Each user has a display of their own gigs
    -  Gigs can be created as a proposal or already confirmed
    -  Users can accept or refuse a gig proposal
    -  Gigs are displayed chronologically
    -  Only display the upcoming gigs
    -  Possibility to view the history of previous gigs

- **Desired Features**
    - Each gig shows a day count until the event
    - Agency fees can vary between the gigs

## Skeleton

A wireframe was created to set the main layout for the software. The header and footer features are fixed, and the content is dynamic: reacts to the user action, based on user type. 

- ### DJ Agenda

Home page where the user's gig id is displayed chronologically.
<details>
<summary>View DJ Agenda Home</summary>

![View Agenda User Home](/docs/images/app_design_home.png)
</details>
<br/>

- ### Gig Details

Details page contains the main info and options.
<details>
<summary>View Gig Details</summary>

![View Gig Details](/docs/images/app_design_home%20(2).png)
</details>
<br/>

## Structure
The project Flamingo is a composition of two apps responsible for different functionality of the website.

- **Agenda App**

Responsible for the gigs management engine, has the models for gigs, venues, and the views, that responsible for **get** information about the gigs and **post** actions to update them.

- **Accounts App**

App that holds the functionality of the user’s authentication and registration management. It also holds the custom model for the user, while the views are responsible for the login, registration, and logout.

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

- The project uses **Poppins** from Google fonts as the first choice, and Sans-serif.

**Images**

- The flamingo on the logo was taken from: [freepng](https://www.freepng.es/)
- The flamingo with sunglasses was taken from: [dreamstime](https://www.dreamstime.com)
- The landing picture was taken from: [Pexels](https://www.pexels.com/)

[**Back to Top**](#table-of-content)

# Features

## Fixed Features

- **Landing Page**

    - Displayed as a standard page for the application when the user is not registered or logged out.

<br/>
<details>
<summary>View Landing Page</summary>

![View Landing Page](/docs/images/flamingLanding.png)
</details>
<br/>

- **Navigation Bar (Header)**
    
    - Appears in every page of the application to support user’s navigation through the website.
    - A Home link that brings directly to the main page of the user
    - Login link to a login form 
    - Register link to a registration form for new users
    - The name “Flamingo” is also a link that redirect to main page
    - When the user is logged in, the word “Welcome” and the username is displayed
    - When the user is logged in, the “Logout” appears which will logout the user and redirect them to the landing page

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

This section is designed to contain all of the main information and tools of the application. The components inside will dynamically change as the user navigates on the website.

### Admin Features

#### Main Page

- **Menu Buttons**
    - Create a Gig links to the page with a form for the creation of a new gig
    - Create a venue links to the page with a form to the creation of a new venue
    - My DJ's is a link for a page with information about all of the registered DJ's
    - Past gigs is a link for a page with information about all of the previous gigs

- **Filter Bar**
    - A section with filters that can be applied to the table, the gigs can be filtered by a DJ, venue and chronologically.
    
- **Table of Gigs**
    - A table where all of the programmed gigs are displayed, in addition to some basic information and a button to bring to a more detailed vision of the gig.

<br/>
<details>
<summary>View Admin Page</summary>

![View Admin Page](/docs/images/flamingoAdminAgenda.png)
</details>
<br/>

#### Create Gig

- Is the page that contains the form to create a gig. The form has a few placeholders to navigate fields easily, additionally some fields with specific data types are arranged to facilitate the usage. At the end of the form, the button “Create” will validate the gig and redirect the user to the main page. Due to the database design, each gig has to have an unique name, only the field “info” can be set as empty. If there are any problems with the validation, the website will display an error message and redirect to the form, while keeping the previously typed data to make the correction easier.

<br/>
<details>
<summary>View Create Gig</summary>

![View Create Gig](/docs/images/flamingoCreateGig.png)
</details>
<br/>

#### Create Venue

- Display a page with a form to create a new venue. All of the fields are a string and the only ones that can be blank are the “website” and “info”.

<br/>
<details>
<summary>View Create Venue</summary>

![View Create Venue](/docs/images/flamingoCreateVenue.png)
</details>
<br/>

#### My Djs

- Display a table with information about each user/DJ who is registered in the application. A button “View Details” is displayed in each row of the table to bring the user to a more informative view of a specific DJ.

<br/>
<details>
<summary>View My Djs</summary>

![View My Djs](/docs/images/flamingoUsersList.png)
</details>
<br/>

#### Manage DJ Account

- A page that displays information about a specific user with a button “Delete User”. The button triggers a modal window asking if the user is sure about the action to delete.

#### Gigs History

- At this page, a table is displayed where each row holds information about the gig that already took place.

<br/>
<details>
<summary>View Gigs History</summary>

![View Gigs History](/docs/images/flamingoAdminHistory.png)
</details>
<br/>

#### Gig Details

- TThis page displays more extensive information about a selected gig. This page uses the same template as the DJ view, only in the case of the admin, there is a button “Edit Gig”, directing the user to a form to edit the gig.

<br/>
<details>
<summary>View Gigs Details</summary>

![View Gigs Details](/docs/images/flamingoGigDetail.png)
</details>
<br/>

#### Update Gig

- This page uses a similar template to the page where the gig is created. However, in addition it  loads the information of the gig, allowing it to be edited. After the alteration has been made, the user may click on the ‘’Update'' button to post the adjustments to the database. On the top, there is a “Delete” button which will trigger a modal to alert the user that the gig will be deleted from the database.

### User as Dj Features

The main page for the DJ user is an agenda: view where the gigs are displayed on cards, ordered by date and holding some essential information and actions for that gig.

#### My gigs agenda

- This is the main page for the DJ user. If the user logged in and has assigned gigs up to come, they will be displayed in cards with different colours depending on the status of the gig (Confirmed, Proposal or Cancelled). Each card holds a button “Details” which will redirect the user to a page with some more information and the possibility of other actions related to the gig. At the top, the button “History” will display the history of the user's gigs.


#### Gigs Cards

- The colour of each of the cards represents their status: green for confirmed, meaning that the admin created an already confirmed gig or that it was accepted by the DJ. Light blue is for a proposal, where the admin is proposing a gig for the DJ which can be accepted or declined. Lastly, red is displayed on a cancelled gig, which for some reason got cancelled by the admin. Gigs rejected by the DJ are not displayed for the DJ user.

<br/>
<details>
<summary>View User's Agenda</summary>

![View User's Agenda](/docs/images/flanigoUserAgenda.png)
</details>
<br/>

#### My gigs history

- This page displays a table with the gigs, date of which is already in the past. This page is only for a quick look at the gigs history and is paginated for a better user experience.


<br/>
<details>
<summary>View User's History</summary>

![View User's History](/docs/images/flamingoUserHistory.png)
</details>
<br/>

#### Gigs Details

- This page displays more information about a selected gig and the venue where it is happening. In the case of being a proposal, the buttons “Accept” or “Reject” are displayed, so the DJ can let the admin know whether the user accepted the gig.

![Gigs Details](/docs/images/flamingoGigsDetails.png)

[**Back to Top**](#table-of-content)

# Testing

- Two approaches were taken during the test routines, one is of a manual testing with the direct use of the features and predicting the correct outcomes, while the other routine was made using **unittest** package and **coverage**.

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

At the moment, no major bug is known or is still not fixed in the application.

## Fixed Detected Bugs

### Admin can delete other admin accounts

- A possible dangerous bug was detected: an admin could delete its own account, leading to a very unexpected behaviour of the application. After identifying the possible bug, changes in the logic were made to fix this behaviour.

### Forms not authenticating

- A major bug occurred during the development, where the forms were not able to authenticate users input. After some research and googling, the line “{csrf_token}” was noticed. After adding the command, the bug was fixed.

### No protected endpoint

- A security breach was detected because any person could just paste the endpoints of the url and could access admin or any user features without authentication. The problem was addressed and all the endpoints for user accounts and admin are protected.

### Styling bugs

- DDue to a change in the font family during the development, some html elements needed to change the style class, in order to keep the layout of the application.

## Detected and not fixed bugs

Some minor styling bugs were detected, however their occurrence does not interfere with the user experience.

### AAdmin list of gigs styling bug

- AAt the main page of the admin user, on the table which displays all of the gigs, some of the list items have a border that’s a little bit thicker than the others, making a slight difference between rolls on the table.

[**Back to Top**](#table-of-content)

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

# Out of Scope User Stories

A feature that would allow the user to have a financial view of the gigs performed was brought to the backlog. However, to keep the application simple so would fit for a MVP, the issue was taken out of the scope. The feature could be implemented in future versions of the app.


# Credits

- A special thank you for the tutors from code institute for the good support when I needed.

- To my mentor Brian O’Hare for the good advises and guidance.

- To the slack community, and specially for those who are there answering questions and helping each other.

[**Back to Top**](#table-of-content)