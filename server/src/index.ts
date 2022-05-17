import cors from 'cors'
import express from 'express'
import { __prod__ } from './constants';
require("dotenv").config();

const main = async () => {
    const app = express()
    app.use(
        cors({
            origin: process.env.CORS_ORIGIN,
            credentials: true,
        })
    );

    app.listen(parseInt(process.env.PORT!), () => {
        console.log(`Server is running on localhost:${process.env.PORT}`)
    })
}

// Add better way to handle exception
main().catch((err) => {
    console.error(err);
});