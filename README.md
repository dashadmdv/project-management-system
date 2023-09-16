# project-management-system
Contract&amp;project management system.

## Contents

* [Technologies](#technologies) 
* [Installing](#installing)
* [Dependencies](#dependencies)
* [Environment variables](#environment-variables)
* [Functionality](#functionality) 
* [Interface](#interface)

## Technologies

* Python 3.10
* PostgreSQL 12

## Installing

To get this project, you need to clone the code from here with:
```bash
  git clone git@github.com:dashadmdv/project-management-system.git
```

## Dependencies

- **datetime**: helps to get current date
- **psycopg2**: PostgreSQL client for Python
- **prettytable**: good-looking database output
- **python-dotenv**: loads environment variables by reading them from a .env file

Install dependencies using:

```bash
  pip install -r requirements.txt
```

## Environment variables

To run this project, you need to set the following environment variables to the **.env** file:

<table>
    <tbody>
        <tr>
            <td>`DB_HOST`</td>
            <td>not required</td>
        </tr>
        <tr>
            <td>`DB_NAME`</td>
            <td>database with that  name is NOT required to exist</td>
        </tr>
        <tr>
            <td>`DB_USER`</td>
            <td rowspan=2>your PostgreSQL username and password (you need <br>to <b>have PostgreSQL installed</b> on your computer)</td>
        </tr>
        <tr>
            <td>`DB_PASSWORD`</td>
        </tr>
    </tbody>
</table>

<b>Place the .env file in the src/ folder!!!</b> Example:
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
