import axios from 'axios';
import {getHeaders} from "@/services/Auth";
import {buildUrl} from "@/services/Base";


export function getGoodsList(){
    return axios.get(
        buildUrl('goods/goods'),
        {
            headers: getHeaders()
        }
    )
}


export function getGood(goodId){
    return axios.get(
        buildUrl(`goods/goods/${goodId}`)
    )
}