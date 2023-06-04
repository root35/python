//-- Initialize Express
const express = require('express');
const app = express();

//-- Create a route
app.get('/hello', (req, res) => {
    res.send('Hello World!');
  });

//-- Use route parameters
//app.get('/users/:userId', (req, res) => {
//  res.send(`User ID is: ${req.params.userId}`);
//});

//-- Start the server
const port = 4000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});


//-- Setup connection between mongodb atlas and expressjs

// Replace this with your MongoDB Atlas connection string
const mongodb_username = 'myriamerakho'
const mongodb_password = 'ABpxTLRxw9qHJWSu'
const mongodb_dburi = "mongodb+srv://myriamerakho:ABpxTLRxw9qHJWSu@cluster0.o1l54uu.mongodb.net/${dbname}?retryWrites=true&w=majority";
const dbname = 'edureka_weather_app'


const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://myriamerakho:ABpxTLRxw9qHJWSu@cluster0.o1l54uu.mongodb.net/?retryWrites=true&w=majority";
// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});
async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);

app.get('/', (req, res) => {
    res.send('Hello, World!');
  });

  
  //-- Schema 
  
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:3000/edureka_weather_app', { useNewUrlParser: true, useUnifiedTopology: true });

const weatherSchema = new mongoose.Schema({
    location: {
      type: String,
      required: true,
    },
    temperature: {
      type: Number,
      required: true,
    },
    condition: {
      type: String,
      required: true,
    },
  });

const Weather = mongoose.model('Weather', weatherSchema);

const weatherEntry = new Weather({ location: 'San Francisco', temperature: 75, condition: 'Sunny' });

weatherEntry.save()
    .then(() => {
        console.log(weatherEntry.location + " saved to weather collection.");
    })
    .catch((error) => {
        console.error(error);
    });

    
//-- Endpoints

const bodyParser = require('body-parser');

const User = mongoose.model('User', new mongoose.Schema({
  username: String,
  password: String  // WARNING: DO NOT STORE PASSWORDS IN PLAIN TEXT IN PRODUCTION
}));

app.use(bodyParser.json());

// Signup
app.post('/signup', async (req, res) => {
  const { username, password } = req.body;

  const user = new User({ username, password });
  await user.save();

  res.status(201).send({ message: 'User created successfully', user });
});

// Signin
app.post('/signin', async (req, res) => {
  const { username, password } = req.body;

  const user = await User.findOne({ username, password });
  if (!user) {
    return res.status(400).send({ message: 'Invalid username or password' });
  }

  res.send({ message: 'User signed in successfully', user });
});

// Get User Data
app.get('/user/:username', async (req, res) => {
  const { username } = req.params;

  const user = await User.findOne({ username });
  if (!user) {
    return res.status(404).send({ message: 'User not found' });
  }

  res.send({ message: 'User fetched successfully', user });
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000')
});

