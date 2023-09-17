# project-management-system
Contract&amp;project management system.

## Contents

* [Technologies](#technologies) 
* [Installing](#installing)
* [Dependencies](#dependencies)
* [Environment variables](#environment-variables)
* [Functionality](#functionality) 
* [Interface](#interface)
* [Program flow (with screenshots)](#program-flow)

## Technologies

* Python
* PostgreSQL

## Installing

To get this project, you need to clone the code from here with:
```bash
  git clone git@github.com:dashadmdv/project-management-system.git
```

## Dependencies

First you should set up the virtual environment in your project. PyCharm automatically suggests 
you to do it and installs all requirements, so you can skip this step if you use PyCharm. 
You can also <a href="https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/" target="_blank">set up and activate venv manually</a>.

- **datetime**: helps to get current date
- **psycopg2**: PostgreSQL client for Python
- **prettytable**: good-looking database output
- **python-dotenv**: loads environment variables by reading them from a .env file

Install dependencies using:

```bash
  pip install -r requirements.txt
```

## Environment variables

To run this project you need to <b>have PostgreSQL installed</b> on your computer. If you don't have PostgreSQL, 
you need to download and run a server (<a href="https://commandprompt.com/education/how-to-download-and-install-postgresql/" target="_blank">Windows</a>, 
<a href="https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql-linux/" target="_blank">Linux</a>, 
<a href="https://www.google.com/search?q=how+to+download+and+install+postgresql" target="_blank">Other OS</a>).

Then you need to set the following environment variables to the **.env** file:

<table>
    <tbody>
        <tr>
            <td>`DB_HOST`</td>
            <td>your database host (most likely 'localhost'), not required</td>
        </tr>
        <tr>
            <td>`DB_NAME`</td>
            <td>database name, not required (the database will be created if not exists)</td>
        </tr>
        <tr>
            <td>`DB_USER`</td>
            <td rowspan=2>your PostgreSQL username and password</td>
        </tr>
        <tr>
            <td>`DB_PASSWORD`</td>
        </tr>
        <tr>
            <td>`DB_PORT`</td>
            <td>your database port (most likely 5432), not required</td>
        </tr>
    </tbody>
</table>

<b>Place the .env file right in the project-management-system/ folder!!!</b> Example:
```bash
DB_HOST = 'localhost'
DB_NAME = 'pmsystem'
DB_USER = 'postgres'
DB_PASSWORD = '12345678'
```

## Functionality


* creating or opening existing database
* creating `projects` and `contracts`
  * contract can be `draft (default)`, `active`, `completed`
  * property `date_of_creation` (today's date) is assigned to project/contract at the moment of creation
  * `contract`'s status can be changed
  * when a `contract` becomes `active`, it gets `date_of_approval` property (today's date)
  * `project` can't be created if there aren't any active `contracts`
* adding `contracts` to `projects`
  * `contract` can be in only one `project`
  * `project` can have many `contracts` (O2M)
  * only an `active` `contract` can be added to a `project`
  * `project` can have only one `active` `contract`
  * we can complete `contract` from the `project` interface
  * we can't add the same `contract` to the `project`

## Interface

Interface structure
* `project`
  * `create` 
  * `add` a `contract` to the project
    * choose the `project` to add contract to
    * choose the `contract` to add
  * `complete` the `contract`
    * choose the `project` with the contract
    * select the `contract` from the list of the chosen project's contracts 
* `contract`
  * `create`
  * `approve` the `contract`
    * select the `contract` from the list of all contracts (NOT through the project)
  * `complete` the `project`
    * select the `contract` from the list of all contracts (NOT through the project)
* `exit`

We also have 'bonus' options that we can get access for from any point of the program:
* see the `list` of all `contracts`
* see the `list` of all `projects`
* go `back`
  * go `back` = `exit` when we are at the start of the program

## Program flow

When the user runs the program, they get greetings and the database status message.
* the database already exists<br>
![Database opening](https://github.com/dashadmdv/project-management-system/assets/69718734/55a679e3-3585-48c3-b01d-88775addb626)
* the database has been created just now<br>
![Database creation](https://github.com/dashadmdv/project-management-system/assets/69718734/aa93a793-6bad-4782-a1c3-5737fa7ddb32)

Then the user gets choice to work with projects or contracts. The user can also choose so-called 'always available operations': show projects/contracts list and go back:<br>
![Always available operations](https://github.com/dashadmdv/project-management-system/assets/69718734/0c6d8f77-dc9d-46b1-8098-99f44cd69508)
If the user is at the start of the program, they can exit:<br>
![Exit from program](https://github.com/dashadmdv/project-management-system/assets/69718734/d68cbd34-f261-4eb3-b1ee-e7c0b9749f48)

If the user chooses to work with projects, they get the following options:
* create project
  * successful creating<br>
  ![Creating a project](https://github.com/dashadmdv/project-management-system/assets/69718734/e11405a2-6612-4f32-884e-7998c92d9263)
  * trying to create project when there are no active contracts
  ![Trying to create a new project when there are no active contracts](https://github.com/dashadmdv/project-management-system/assets/69718734/0151ad9c-fcbb-4e21-8a01-375687b0cf0e)
* add a contract to the project
  * successful adding<br>
  ![Adding an active contract to the project](https://github.com/dashadmdv/project-management-system/assets/69718734/426067a4-97b4-44ca-8eed-930bc5848213)
  You can see that the added contract gets the id of the parent project stored.
  * trying to add to a project that already has an active contract<br>
  ![Trying to add new contract to a project that already has an active contract](https://github.com/dashadmdv/project-management-system/assets/69718734/d476e8a5-3874-43c6-95cb-d8edbc0d226c)
  * trying to add the contract that is already used in another project<br>
  ![Trying to add to a project the contract that is already used in another project](https://github.com/dashadmdv/project-management-system/assets/69718734/6d49f48e-ee12-4d54-978e-3d5a1f38cb7c)
  * trying to add inactive contract to the project<br>
  ![Trying to add inactive contract to the project](https://github.com/dashadmdv/project-management-system/assets/69718734/075d5fab-d6a3-4710-bcc7-9d877173802e)
* complete the contract
  * successful completing<br>
  ![Successful project completing](https://github.com/dashadmdv/project-management-system/assets/69718734/9fa69c82-f9aa-4397-acf0-374141f2d1ff)
  * trying to complete an already completed project<br>
  * ![Trying to complete an already completed project](https://github.com/dashadmdv/project-management-system/assets/69718734/eb29203b-fb9b-40db-886c-0e3e5b410632)

If the user chooses to work with contracts, they get the following options:
* create contract<br>
![Creating a contract](https://github.com/dashadmdv/project-management-system/assets/69718734/0a25ecd2-f3aa-4348-8bcf-096aa9407946)
You can see that contract is created as the draft, and it doesn't have the date of approval since it's not active.
* approve the contract
  * successful approving<br>
  ![Approve the contract](https://github.com/dashadmdv/project-management-system/assets/69718734/87d587cd-8930-4abe-b545-cb592036ad8a)
  You can see that contract got the date of approval along with the `active` status.
  * trying to approve the already approved contract<br>
  ![Trying to aprove the already approved contract](https://github.com/dashadmdv/project-management-system/assets/69718734/8f4e00c6-772a-47cd-80af-26a6f84c67f9)
* complete the contract
  * successful completing<br>
  ![Complete the contract](https://github.com/dashadmdv/project-management-system/assets/69718734/cc872586-c662-456e-a526-43d827852956)
  * trying to complete the already completed contract<br>
  ![Trying to complete the already completed contract](https://github.com/dashadmdv/project-management-system/assets/69718734/f43d81b7-3957-4b6d-8a28-6c050d3b9264)
