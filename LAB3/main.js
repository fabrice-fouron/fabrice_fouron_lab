const express = require('express');
const path = require('path');
const cookieParser = require('cookie-parser');

const app = express();
const PORT = 3000;

app.use(express.json());

app.use(express.static(path.join(__dirname, 'public')));

app.use(cookieParser())

// 5 HTML routes
app.get('/', (req, res) => {
    res.status(200);
    res.send("<h1>welcome to root URL of Server</h1>");
});


app.get('/about', (req, res) => {
    res.status(200);
    res.send("<p>This is content for that talks about the main purpose of this project.</p>");
});

app.get('/comment', (req, res) => {
    res.status(200);
    res.send("<p>Enter a comment you want</p><br/><textarea></textarea>")
})

app.get('/italic', (req, res) => {
    res.status(200);
    res.send('<p><em>This is a text in italic</em></p>')
})

app.get('/helloworld', (req, res) => {
    res.status(200);
    res.send('<h4>404 - There is no error</h4></br><button>And this is a button</button>')
})

// query parameters
app.get('/home/:new_text', (req, res) => {
    const temp = req.params.new_text;
    res.status(200);
    res.send(`<h2>This is the new text being printed out: ${temp}</h2>`);
});


app.get('/info/:firstname/:lastname', (req, res) => {
    const first_name = req.params.firstname;
    const last_name = req.params.lastname;
    res.status(200);
    res.send(`First Name: ${first_name} - Last Name: ${last_name}`);
});

app.get('/product/:type/:name', (req, res) => {
    const type = req.params.type;
    const name = req.params.name;

    res.status(200);
    res.send(`This is a type of ${type} that is called a ${name}`)
});

app.get('/movie/:name/:rating', (req, res) => {
    const movieName = req.params.name;
    const movieRating = req.params.rating;

    res.status(200);
    res.send(`I rate the movie ${movieName} a ${movieRating}/10`)
});

app.get('/search/:email', (req, res) => {
    const emailAddress = req.params.email;
    const addresses = ['hello@world', 'fouronf@wit.edu']
    res.status(200);
    if (addresses.includes(emailAddress))
        res.send(`<h3>Your email address was found.</h3>`);
    else
        res.send("<h3>This address does not exist...</h3>");
});

// header parameter
app.get('/headers', (req, res) => {
    const head = req.headers['role'];

    res.status(200);
    res.send(`This is the user role header parameter: ${head}`);
});


// Cookies
app.get('/set-cookie', (req, res) => {
    res.cookie('username', 'CookieValue', {
        expire: 1000 * 60 * 60 * 24
    });

    res.send('The cookie was set!');
})

app.get('/cookie', (req, res) => {
    res.status(200);
    res.send(`This is the cookies: ${req.cookies['username']}`);
});

// body input
app.post('/user-input', (req, res) => {
    const userInput = req.body.message;
    res.status(200);
    res.send(`This is what the user sent: ${userInput}`);
});


app.listen(PORT, (error) => {
    if(!error) {
        console.log("No errors");
    }
    else {
        console.log("There is an error!!");
    }
});
