import User from '../models/user.model.js';
import bcryptjs from 'bcryptjs';
import { errorHandler } from '../utils/error.js'

export const signup = async (req, res, next) => {
    const { username, email, password } = req.body;
    const hashedPasssword = bcryptjs.hashSync(password,10);
    const newUser = new User({ username, email, password:hashedPasssword });

    try{
        await newUser.save();
        res.status(201).json('User created sucessfully!');
    }
    catch(error){
        next(errorHandler(550, 'error from the function signup'));
    }
    
};