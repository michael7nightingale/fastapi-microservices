import {meUser} from "@/services/UserService";
import axios from "axios";
import {buildUrl} from "@/services/Base";

export function setUser(token){
    localStorage.user = token;
     axios.get(
        buildUrl('users/me'),
        {
            headers: getHeaders()
        }
     )
         .then((response) =>
         localStorage.userData = JSON.stringify(response.data));
    return meUser().then((response) => {
        localStorage.userData = JSON.stringify(response.data);
    })

}



export function getHeaders(){
    let user = localStorage.user;
    let headers = {};
    if (user){
        headers['Authorization'] = `Token ${user}`;
    }
    return headers
}


export function logoutUser(){
    localStorage.removeItem("user");
    localStorage.removeItem("userData")
}


export function getUser(){
    return localStorage.getItem("userData");
}