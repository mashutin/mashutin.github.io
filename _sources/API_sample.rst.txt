========================
Sample API documentation
========================

.. note::

   This sample is a part of a fictional API reference for the non-existent "SuperTrader" platform. It describes the API methods available for the 'Account' object.

Account
=======

The Account object represents a trading account. An Account is owned by one user (Account Owner).

Getting a list of accounts
--------------------------

:GET /accounts:
   Returns a list of all trading accounts with their details.

Query string parameters
~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :widths: auto
   :header-rows: 1
   :stub-columns: 1

   Parameter,Required/Optional,Description,Data type
   limit,optional,The maximum number of accounts to return.,integer

Request example
~~~~~~~~~~~~~~~

::

   curl -i -X GET “https://api.supertrader.com/1.0/accounts?limit=50” \
      -H “Authorization: Bearer token12345”

Response example
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
      "entries": [
         {
            "account_id": 12345,
            "account": 5432674321,
            "online": true,
            "account_status": "demo",
            "name": "Denis",
            "last_name": "Mashutin",
            "city": "Moscow",
            "state": "Moscow",
            "country": "Russia",
            "post_code": 108842,
            "comment": "Very good account"
         },
         {
            "account_id": 98765,
            "account": 456353535,
            "online": true,
            "account_status": "demo",
            "name": "Denis",
            "last_name": "Mashutin",
            "city": "Scherbinka",
            "state": "Moscow",
            "country": "Russia",
            "post_code": 101621,
            "comment": "Even better account"
         }
      ]
   }

Modifying an account
--------------------

:PUT /accounts/{account_id}:
   Modifies the account by updating its details. Returns the updated account details.

Path parameters
~~~~~~~~~~~~~~~

.. csv-table::
   :widths: auto
   :header-rows: 1
   :stub-columns: 1

   Path parameter,Description
   {account_id},The ID of the account that you want to modify.

Request body
~~~~~~~~~~~~

.. csv-table::
   :widths: auto
   :header-rows: 1
   :stub-columns: 1

   Field,Required/Optional,Description,Data type
   online,optional,Specifies if the account is displayed as online.,boolean
   account,optional,The number of the trading account.,integer/uint
   account_status,optional,The Access Rights type of the account.,string
   name,optional,The first name of the account owner.,string
   last_name,optional,The last name of the account owner.,string
   city,optional,The city of residence of the account owner.,string
   state,optional,The state of residence of the account owner.,string
   country,optional,The country of residence of the account owner.,string
   post_code,optional,The postal code of the account owner.,integer/uint
   comment,optional,The text of the admin comment.,string

Request example
~~~~~~~~~~~~~~~

::

   curl -i -X PUT “https://api.supertrader.com/1.0/accounts/12345” \
      -H “Authorization: Bearer token12345” \
      -H “Content-Type”: application/json” \
      -d ‘{
         “comment”: “The best account ever!”
      }’

Response example
~~~~~~~~~~~~~~~~

.. code-block:: json

   {
      "account_id": 12345,
      "account": 5432674321,
      "online": true,
      "account_status": "demo",
      "name": "Denis",
      "last_name": "Mashutin",
      "city": "Moscow",
      "state": "Moscow",
      "country": "Russia",
      "post_code": 108842,
      "comment": "The best account ever!"
   }