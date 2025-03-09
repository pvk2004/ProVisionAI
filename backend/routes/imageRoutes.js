// filepath: /backend/routes/imageRoutes.js
const express = require('express');
const { annotateImage } = require('../services/visionService');
const router = express.Router();

router.post('/annotate', async (req, res) => {
    const imageData = req.body.image;
    try {
        const annotation = await annotateImage(imageData);
        res.json(annotation);
    } catch (error) {
        res.status(500).json({ error: 'Failed to annotate image' });
    }
});

module.exports = router;