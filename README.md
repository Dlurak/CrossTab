# Crosstab

CrossTab allows you to share tabs between devices.

## How it works?

- You can send an URL to CrossTab
- CrossTab stores that as the shareurl
- You can open `url/redirect` to let you redirect to the shareurl

### URIs

CrossTab has the following endpoints:

| URI         | Method | Description                                       |
| ----------- | ------ | ------------------------------------------------- |
| `/`         | `GET`  | Simply get the redirect url as the body           |
| `/`         | `POST` | Put the url of the request body into the shareurl |
| `/redirect` | `GET`  | Redirect to the shareurl                          |
| `/ui`       | `GET`  | Get a simple UI to controll CrossTab              |

## Getting-Started

You need to self-host crosstab, I use a Raspberry Pi but your daily driver should also be fine!

### From Docker-hub

1. Pull the image from docker hub
   ```bash
   docker pull dlurak/crosstab
   ```
2. Start it
   ```bash
   docker run -d -p 5000:5000 dlurak/crosstab
   ```

### From source

1. Clone this repo
   ```bash
   git clone https://github.com/Dlurak/CrossTab.git
   ```
2. Start it using docker
   ```bash
   cd api/
   docker-compose up
   ```
3. It runs on [localhost port 5000](localhost:5000)

Please note that everyone who can access your server will be able to see which website you share and also to change which website you want to open.  
So make sure only trusted people can access the server!

## Integration

### iOS

There is [this](https://www.icloud.com/shortcuts/f47341e1049247b9b18a52ec16d73e3c) siri shortcut to share a site to CrossTab directly from the sharesheet.
