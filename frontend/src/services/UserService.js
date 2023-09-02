import axios from 'axios';
import {getHeaders} from "@/services/Auth";
import {buildUrl} from "@/services/Base";


export function loginUser(email, password){
    let data = {
        email: email,
        password: password
    }
    return axios.post(
         buildUrl('users/token/'),
        data
    )
}



export function registerUser(data){
    return axios.post(
        buildUrl('users/register/'),
        data
    )
}


export function meUser(){
    return axios.get(
        buildUrl('users/me/'),
        {
            headers: getHeaders()
        }
    )
}
