# The Poet 

## Challenge Description

a. Using Angular if possible or javascript or typescript, complete the following and be ready to execute and explain your work during the interview:

b. Review the  https://poetrydb.org/ api.

c. Write a script or webpage to make rest calls to the server (author and title endpoint) and inspect the response.

d. The script should throw an error if a 200 is not received.

e. Enhance the script to retrieve both author and title by name and log all relevant data.

f. Be prepared to expand the functionality of your solution during the interview.

## Running the Code
This webpage was developed in Angular 20.2.0 with Node.js v22.18.0. From this directory, run the following:

`cd poetry-api`

`ng serve`

This will put you in the Angular directory and deploy the webpage to `http://localhost:4200`.

## Using the Webpage
The webpage has two input boxes. One is to search by Author and the other is to search by Title.

If searching by Title, the returned result will be all (non-exact) matching titles along with the authors of those titles.

If searching by Author, the returned result will be all (non-exact) matching authors along with the titles written by those authors.

Only the first 1000 characters of the result will be displayed in the webpage. If this truncates the result, the full return value can be found by inspecting the Console or Network tab of the Developer Tools panel.

An error message is displayed if the returned status is not 200.