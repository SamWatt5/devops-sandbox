# Flask app contained in a docker container!
## How it works
Basic flask app that retrieves results from a useless facts API.
This is containerized using Docker to ensure the app runs on all systems.
I then used nginx as a reverse proxy, so that the app can be found from localhost/fact, instead of localhost:5000/fact. This isnt in the repo but its fun to do!
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

To get nginx working as a reverse proxy, you have to do the following...
1. Find your nginx config, mine was at /etc/nginx/sites-available/default
2. Find the "location section"
3. Inside, add the line `proxy_pass http://localhost:5000`
4. Reload nginx with
```bash
sudo systemctl reload nginx
```
5. TA-DA! It's (hopefully) working!! go to `http:localhost/fact` for a fun fact!!

## Takeaways
I had a fun afternoon putting this together! I had never used docker or nginx before, so used this mini-project as a learning tool for the (very) basics.
I used a Ubuntu server hosted on a virtual machine, which I SSH'ed into, which was a fun challenge in itself!

