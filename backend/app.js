// filepath: /backend/app.js
const express = require('express');
const bodyParser = require('body-parser');
const imageRoutes = require('./routes/imageRoutes');

const app = express();
app.use(bodyParser.json());

app.use('/api', imageRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});