Running Tests:
    `py -m unittest discover test`

Running Application:
    `py main.py -url <start url>`

General Flow:
1. Make request to URL.
2. Check request is 200 OK
3. Match all URLs from page
4. Filter URLs which are invalid in format
5. Filter URLs which are not on same subdomain
6. Filter URLs which have already been visited
7. Go to remaining URLS
8. Repeat.