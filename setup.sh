#!/bin/sh

# Reference: https://knowledge.udacity.com/questions/537344
# export AUTH0_DOMAIN = "dev-dudattxg70vfdgkq.au.auth0.com"
# export ALGORITHMS = ["RS256"]
# export API_AUDIENCE = "coffeeshop"

export DATABASE_URI="postgresql://postgres:postgres@localhost:5432/capstone"
export FLASK_APP=flaskr
export FLASK_DEBUG=True
export FLASK_ENVIRONMENT=debug
