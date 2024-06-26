#!/bin/sh

# Ref: https://knowledge.udacity.com/questions/724461
# export SECRET=""
export ASSISTANT_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhkVlVnQnBBdXoxZXVMSHB5Q1REaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1kdWRhdHR4ZzcwdmZkZ2txLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjZlOWU1MGJlNzQ5YWZhYWEyOWI2NWIiLCJhdWQiOiJjYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNzE4NjIzMTU4LCJleHAiOjE3MTg2MzAzNTgsInNjb3BlIjoiIiwiYXpwIjoidDRvU2toWmhndFRpQTlUY3kxZVI2ZUVZaUY4OFF0WGciLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.ldJXiwuZTSXprT_sC0HoQrQR9xLf8ZElb--NYS1UtZV8gY2NoylKlZ3CJ-ZIct8DkbJ_6YoUqybjXZ4wWCEU-0TtNH-J7nOoW7_b2iu0iHFDwFnW6_IMJZlRwJw7VubHRbq0MxkO4kgWbYEauFImDNLjIhK4F72tddI40UacxJj-Ve-Hjbx8iXoKU8sH-QDRlsf8NW-yaXqAUmTKCbRv7Ay918MVW36reNJxOKVPoxGvJvRQ3JjFOh0mM_hUuQz-FXSAXXwhJQC4Y9UkGggr2hC2HZmLQkMVPr2KgWVsxBe5ZqTl9sowOXKZsGvOXV3VEzxJ-TbkBmceb6_SBqTMFg"
export DIRECTOR_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhkVlVnQnBBdXoxZXVMSHB5Q1REaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1kdWRhdHR4ZzcwdmZkZ2txLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjZlOWY1NDA5MGYyMzM0YjczY2MxZmQiLCJhdWQiOiJjYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNzE4NjIzMTgzLCJleHAiOjE3MTg2MzAzODMsInNjb3BlIjoiIiwiYXpwIjoidDRvU2toWmhndFRpQTlUY3kxZVI2ZUVZaUY4OFF0WGciLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwicG9zdDphY3RvcnMiLCJwb3N0OmNhc3RfYWN0b3JzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.dV4iWlAF795S6qqv1dNXMIKl-GL-vAn_vxUukQs6kKyHjTT17qdSH0goAY2o0uA-v9W2_cB60FhUu8pMfbaJsnkoL9lkFjc218WaPZM67YQCSwb_Y2UZ9gUuuMYrWOzTf842GGgCDPpXU6cQJN9UtMa6IWF7M1hFsLIY-HdS7hKQJ5X_spyA4wX9Tv57kCnswoQHfXIE4C-Ezr8kH7b7HqiwPg5p-eAqTs84rmK8QFvUS3nVQI0uaeYcBNsWRuF1fwoSZeF0qbpvmo1mwPW-ktPmMdb0eQDtCl6uX_cNoiDSExgaXWy-YfFrqYdyOstSsM7YlVMXt0-m_zhNxyN9Ng"
export PRODUCER_TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhkVlVnQnBBdXoxZXVMSHB5Q1REaiJ9.eyJpc3MiOiJodHRwczovL2Rldi1kdWRhdHR4ZzcwdmZkZ2txLmF1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NjZlOWY5NTg4ZjJlODZhZjRmOWVlZmYiLCJhdWQiOiJjYXN0aW5nQWdlbmN5QVBJIiwiaWF0IjoxNzE4NjIzMjE4LCJleHAiOjE3MTg2MzA0MTgsInNjb3BlIjoiIiwiYXpwIjoidDRvU2toWmhndFRpQTlUY3kxZVI2ZUVZaUY4OFF0WGciLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpjYXN0X2FjdG9ycyIsInBvc3Q6bW92aWVzIiwidXBkYXRlOmFjdG9ycyIsInVwZGF0ZTptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.wnHE-f4AjVC3fmEBklu2R3VzakahaefY6YdRzE5P19svar8j_IDe0dH7_65nJpNwJOilwH4AWVyBrc6dfzWF3kVrZ1vcljItrAASY_DuJ9ZOrvbWTbJpBHN0_Pknjz6ngtgWGSd-Ph6b5Qan7j9isIT4dE5YGnTG-_wEUHLRgSVe4vv0FO5y-Kk4OUgUGBXtIw6tUskdZhgaWaEVcvnGwqojCe3xjEoSmCHwgeKMIuLUqAy-GkIBFqQYOKuBYeJfHFNAQroC84JQWwqOD67NZ2sd4y2AVzAXwUL_JWSsZKjOFGHDREh-d7gyVITSu0f3UWG61nda4APw3pxpw8GhGg"

# Reference: https://knowledge.udacity.com/questions/537344
export AUTH0_DOMAIN="dev-dudattxg70vfdgkq.au.auth0.com"
export ALGORITHMS=["RS256"]
export API_AUDIENCE="castingAgencyAPI"

export DATABASE_URL="postgresql://postgres:postgres@localhost:5432/capstone"
export FLASK_APP=app
export FLASK_DEBUG=True
export FLASK_ENVIRONMENT=debug

export TEST_DATABASE_URI="postgresql://postgres:postgres@localhost:5432/capstone_test"
