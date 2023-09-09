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


export function getBasket(){
    return axios.get(
        buildUrl("goods/baskets/current"),
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
        buildUrl(`goods/baskets/current/goods`),
         data,
        {
            headers: getHeaders()
        }
    )
}


export function updateCartGood(basketGoodId, amount){
    let data = {
        amount: amount
    }
    return axios.patch(
        buildUrl(`goods/baskets/current/goods/${basketGoodId}`),
        data,
        {
            headers: getHeaders()
        }
    )
}


export function deleteCartGood(basketGoodId){
    return axios.delete(
        buildUrl(`goods/baskets/current/goods/${basketGoodId}`),
        {
            headers: getHeaders()
        }
    )
}

export function showPrice(price, discount){
      return price * (1 - (discount / 100))
    }
