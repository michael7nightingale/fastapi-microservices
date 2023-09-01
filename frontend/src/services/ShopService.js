import axios from 'axios';
import {getHeaders} from "@/services/Auth";
import {buildUrl} from "@/services/Base";


export function getGoodsList(){
    let data = {
        username: username,
        password: password
    }
    return axios.post(
         buildUrl('auth/token/'),
        data,
        {
            headers: getHeaders()
        }
    )
}
