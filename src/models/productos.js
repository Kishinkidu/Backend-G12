import mongoose from "mongoose";

const productos = new mongoose.Schema({
    nombre: {
        type: mongoose.SchemaTypes.String,
        required: true
    },
    precio: mongoose.SchemaTypes.Decimal128,
    disponible:{
        type: mongoose.SchemaTypes.Boolean,
        default: true,
    },
});

export const producto = mongoose.model("productos", productos);