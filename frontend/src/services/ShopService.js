import axios from 'axios';
import {getHeaders} from "@/services/Auth";
import {buildUrl} from "@/services/Base";
import {assertCallerMetadata} from "@babel/core/lib/config/validation/option-assertions";


export function getGoodsList(){
    return axios.get(
        buildUrl('goods/goods'),
        {
            headers: getHeaders()
        }
    )
}

export function getGoodsListByCategory(categoryId){
    return axios.get(
        buildUrl(`goods/categories/${categoryId}/goods`),
        {
            headers: getHeaders()
        }
    )
}


export function getGoodsListBySubcategory(subcategoryId){
    return axios.get(
        buildUrl(`goods/subcategories/${subcategoryId}/goods`),
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


export function getGoodDescriptionTags(goodId){
    return axios.get(
        buildUrl(`goods/goods/${goodId}/description-tags`)
    )
}


export function getCategories(){
     return axios.get(
        buildUrl(`goods/categories`),
        {
            headers: getHeaders()
        }
    )
}

export function getCategory(categoryId){
    return axios.get(
        buildUrl(`goods/categories/${categoryId}`),
        {
            headers: getHeaders()
        }
    )
}


export function getSubcategory(subcategoryId){
    return axios.get(
        buildUrl(`goods/subcategories/${subcategoryId}`),
        {
            headers: getHeaders()
        }
    )
}


export function addToCart(goodId, amount){
    let data = {
        good: goodId,
        amount: amount
    }
     return axios.post(
        buildUrl(`orders/basket/goods`),
         data,
        {
            headers: getHeaders()
        }
    )
}
