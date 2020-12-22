# graphql-leader-board
A graphql API to manage a leaderboard.

## Architecture 
This API is implemented using AWS AppSync which resolves the graphql queries and mutations using AWS Lambda function backed by AWS Dynamodb.

## AWS Lambda
The AWS Lambda function is implemented in python using [sleemo](https://github.com/twkiiim/sleemo) library to facilitate AWS AppSync.

## GraphQL
Endpoint: https://jnkbz3qi7bhm7cu5tf2klsseey.appsync-api.us-east-1.amazonaws.com/graphql

Authentication: API KEY

### Schema
```
schema {
  query: Query
  mutation: Mutation
}

type Mutation {
  addPoint(input: AddPointInput!): Boolean!
  createUser(input: CreateUserInput!): User
  deleteUser(input: DeleteUserInput!): Boolean!
  resetAllUsers: Boolean!
  subPoint(input: SubPointInput!): Boolean!
}

type Query {
  getUser(id: ID!): User
  listUsers: [User]
}

type User {
  address: String
  age: Int
  id: ID!
  name: String
  points: Int
}

input AddPointInput {
  id: ID!
}

input CreateUserInput {
  address: String
  age: Int
  name: String
}

input DeleteUserInput {
  id: ID!
}

input SubPointInput {
  id: ID!
}

```

## Curl Examples
Note: Replace `API-KEY-VALUE` with the provided key.

### Create a user
```
curl -H "Content-Type:application/graphql" -H "x-api-key:API-KEY-VALUE" -d '{ "query": "mutation {createUser(input: {name: \"my name\", address: \"my address\", age: 20}) {id name age points}}"}' https://jnkbz3qi7bhm7cu5tf2klsseey.appsync-api.us-east-1.amazonaws.com/graphql 
```
Response:
```
{
    "data": {
        "createUser": {
            "id": "ff8fa1f5-caa0-4092-b87b-c0d60a1f1ca0",
            "name": "my name",
            "age": 20,
            "points": 0
        }
    }
}
```
### List All Users
```
curl -H "Content-Type:application/graphql" -H "x-api-key:API-KEY-VALUE" -d '{ "query": "{listUsers {id name age points address } }"}' https://jnkbz3qi7bhm7cu5tf2klsseey.appsync-api.us-east-1.amazonaws.com/graphql 
```
Response:
```
{
    "data": {
        "listUsers": [
            {
                "id": "131fb9ff-0d56-42fe-8d9b-b8481b03294a",
                "name": "user1",
                "age": 83,
                "points": 0,
                "address": "nowhere"
            },
            {
                "id": "d44446cf-5279-4ffa-8667-51acb041c5cf",
                "name": "test-user",
                "age": 83,
                "points": 0,
                "address": "nowhere"
            },
            {
                "id": "31007ee5-d3e7-45ac-b69b-8c31b90995a2",
                "name": "user3",
                "age": 83,
                "points": 0,
                "address": "nowhere"
            }
        ]
    }
}
```
### Get one User
```
curl -H "Content-Type:application/graphql" -H "x-api-key:API-KEY-VALUE" -d '{ "query": "query {getUser(id: \"515e5f7c-6995-4480-953a-90279210581b\") {id name age points address }}"}' https://jnkbz3qi7bhm7cu5tf2klsseey.appsync-api.us-east-1.amazonaws.com/graphql 

```
Response:
```
{
    "data": {
        "getUser": {
            "id": "515e5f7c-6995-4480-953a-90279210581b",
            "name": "test-user",
            "age": 83,
            "points": 0,
            "address": "nowhere"
        }
    }
}
```
### Add a Point to a User
```
curl -H "Content-Type:application/graphql" -H "x-api-key:API-KEY-VALUE" -d '{ "query": "mutation {addPoint(input: {id: \"515e5f7c-6995-4480-953a-90279210581b\"})}"}' https://jnkbz3qi7bhm7cu5tf2klsseey.appsync-api.us-east-1.amazonaws.com/graphql 
```
Response:
```
{"data":{"addPoint":true}}
```
### Remove a Point from a User
```
curl -H "Content-Type:application/graphql" -H "x-api-key:API-KEY-VALUE" -d '{ "query": "mutation {subPoint(input: {id: \"515e5f7c-6995-4480-953a-90279210581b\"})}"}' https://jnkbz3qi7bhm7cu5tf2klsseey.appsync-api.us-east-1.amazonaws.com/graphql 
```
Response:
```
{"data":{"subPoint":true}}
```
### Reset Points for All Users
```
curl -H "Content-Type:application/graphql" -H "x-api-key:API-KEY-VALUE" -d '{ "query": "mutation {resetAllUsers}"}' https://jnkbz3qi7bhm7cu5tf2klsseey.appsync-api.us-east-1.amazonaws.com/graphql 
```
Response:
```
{"data":{"resetAllUsers":true}}
```


