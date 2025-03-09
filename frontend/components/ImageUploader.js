// filepath: /frontend/components/ImageUploader.js
import { annotateImage } from '../services/api';
import { useState } from 'react';

const ImageUploader = () => {
    const [annotation, setAnnotation] = useState(null);

    const handleUpload = async (event) => {
        const file = event.target.files[0];
        const reader = new FileReader();
        reader.onloadend = async () => {
            const imageData = reader.result;
            const annotation = await annotateImage(imageData);
            setAnnotation(annotation);
        };
        reader.readAsDataURL(file);
    };

    return (
        <div>
            <input type="file" onChange={handleUpload} />
            {annotation && <div>{JSON.stringify(annotation)}</div>}
        </div>
    );
};

export default ImageUploader;