// filepath: /frontend/services/api.js
export const annotateImage = async (imageData) => {
    const response = await fetch('/api/annotate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: imageData })
    });
    return response.json();
};