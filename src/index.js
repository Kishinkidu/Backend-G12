import express from 'express';
import mongoose from 'mongoose';
import { producto } from './models/productos.js';


const servidor = express();
const PORT = process.env.PORT ?? 3000;



servidor .get("/", (req, res) =>{
    return res.status(200).json({
        message:"Bienvenido a m API con MongoDb"
    })
});

servidor.listen(PORT, async ( )=>{
    console.log(`Servidor conectado al puerto ${PORT}`);
    mongoose.connect(process.env.DATABASE_URL);
    console.log('Base de datos conectada exitosamente');
});