# Flask app contained in a docker container!
## How it works
Basic flask app that retrieves results from a useless facts API.
This is containerized using Docker to ensure the app runs on all systems.
I then used nginx as a reverse proxy, so that the app can be found from localhost/fact, instead of localhost:5000/fact.
I then used a docker compose YAML file to automate the docker build/run system!
### How to run
To run this, you need to do a docker build command, like so...
```bash
docker build -t fact-app .
```

Now that the container has been built, it needs to be ran, like so...
```bash
docker run -p 5000:5000 fact-app
```
or even better:
```bash
docker run -d -p 5000:5000 fact-app
```
(this one lets you keep using the terminal whilst its running!)

NOTE: You can also use docker compose, by running:
```bash
docker compose up
```
This means you dont need to build and run the docker container separately, as it does it for you!

To get nginx working as a reverse proxy, you have to do the following...
1. Find your nginx config, mine was at /etc/nginx/sites-available/default
2. Find the "location section"
3. Inside, add the line `proxy_pass http://localhost:5000`
4. Reload nginx with
```bash
sudo systemctl reload nginx
```
5. TA-DA! It's (hopefully) working!! go to `http:localhost/fact` for a fun fact!!

(My nginx config file is found in `nginx/default.conf`)

## Takeaways
I had a fun afternoon putting this together! I had never used docker or nginx before, so used this mini-project as a learning tool for the (very) basics.
I used a Ubuntu server hosted on a virtual machine, which I SSH'ed into, which was a fun challenge in itself!

