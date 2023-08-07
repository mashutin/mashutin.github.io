# Sample API documentation

> This sample is a part of a fictional API reference for the non-existent "SuperTrader" platform. It describes the API methods available for the 'Account' object.
> 
{style="note"}

The ``Account`` object represents a trading account. An ``Account`` is owned by one user (``Account Owner``).

## Getting a list of accounts

{style="medium"}
GET /accounts
: Returns a list of all trading accounts with their details.

### Query string parameters

<table style="both">
<tr>
<td>Parameter</td>
<td>Required/Optional</td>
<td>Description</td>
<td>Data type</td>
</tr>
<tr>
<td>limit</td>
<td>optional</td>
<td>The maximum number of accounts to return.</td>
<td>integer</td>
</tr>
</table>

### Request example

```
curl -i -X GET “https://api.supertrader.com/1.0/accounts?limit=50” \
  -H “Authorization: Bearer token12345”
```

### Response example

```
{
  "entries": [
     {
        "account_id": 12345,
        "account": 5432674321,
        "online": true,
        "account_status": "demo",
        "name": "John",
        "last_name": "Smith",
        "city": "New York",
        "state": "NY",
        "country": "US",
        "post_code": 10001,
        "comment": "Demo account"
     },
     {
        "account_id": 98765,
        "account": 456353535,
        "online": true,
        "account_status": "demo",
        "name": "Jane",
        "last_name": "Doe",
        "city": "Austin",
        "state": "TX",
        "country": "US",
        "post_code": 73301,
        "comment": "Demo account"
     }
  ]
}
```
{lang="json"}

## Modifying an account

{style="wide"}
PUT /accounts/\{account_id}
: Modifies the account by updating its details. Returns the updated account details.

### Path parameters

<table style="both">
<tr>
<td>Path parameter</td>
<td>Description</td>
</tr>
<tr>
<td>{account_id}</td>
<td>The ID of the account that you want to modify.</td>
</tr>
</table>

### Request body

<table style="both">
<tr>
<td>Field</td>
<td>Required/Optional</td>
<td>Description</td>
<td>Data type</td>
</tr>
<tr>
<td>online</td>
<td>optional</td>
<td>Specifies if the account is displayed as online.</td>
<td>boolean</td>
</tr>
<tr>
<td>account</td>
<td>optional</td>
<td>The number of the trading account.</td>
<td>integer/uint</td>
</tr>
<tr>
<td>account_status</td>
<td>optional</td>
<td>The Access Rights type of the account.</td>
<td>string</td>
</tr>
<tr>
<td>name</td>
<td>optional</td>
<td>The first name of the account owner.</td>
<td>string</td>
</tr>
<tr>
<td>last_name</td>
<td>optional</td>
<td>The last name of the account owner.</td>
<td>string</td>
</tr>
<tr>
<td>city</td>
<td>optional</td>
<td>The city of residence of the account owner.</td>
<td>string</td>
</tr>
<tr>
<td>state</td>
<td>optional</td>
<td>The state of residence of the account owner.</td>
<td>string</td>
</tr>
<tr>
<td>country</td>
<td>optional</td>
<td>The country of residence of the account owner.</td>
<td>string</td>
</tr>
<tr>
<td>post_code</td>
<td>optional</td>
<td>The postal code of the account owner.</td>
<td>integer/uint</td>
</tr>
<tr>
<td>comment</td>
<td>optional</td>
<td>The text of the admin comment.</td>
<td>string</td>
</tr>
</table>

### Request example

```
curl -i -X PUT “https://api.supertrader.com/1.0/accounts/12345” \
  -H “Authorization: Bearer token12345” \
  -H “Content-Type”: application/json” \
  -d ‘{
     “comment”: “The best account ever!”
  }’
```
{lang="curl"}

### Response example

```
{
  "account_id": 12345,
  "account": 5432674321,
  "online": true,
  "account_status": "demo",
  "name": "John",
  "last_name": "Smith",
  "city": "New York",
  "state": "NY",
  "country": "US",
  "post_code": 1001,
  "comment": "The best account ever!"
}
```
{lang="json"}