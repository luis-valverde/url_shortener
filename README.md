# URL Shortener

## Table Of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Open API Documentation](#documentation)

## Introduction

Spice up your life with your very own URL shortener! You may have used or created links via
services like bit.ly before. The goal is to turn a potentially long URL into a much shorter one,
for ease of use. Now it's time to make your own.

## Requirements

Create the necessary APIs to satisfy the following:

1. Receive a URL and return a unique short-form URL for an specific domain.
2. Receive a short URL and return the original long URL.
3. Be fairly certain that these functions work as expected.

**Bonus**: Count the number of times each short URL was "visited", that is, resolved back to
return the original, as per point 2 above.

## How to Run

From the Terminal, navigate to the folder on your machine where you've put the project directory, and then
run these commands:

```bash
docker-compose -f local.yml build
docker-compose -f local.yml up
```

After that, the server should be running on: http://0.0.0.0:8000/

## Open API Documentation

There is a basic Open API documentation using this link: http://localhost:8000/docs/

There you can check the available APIs.