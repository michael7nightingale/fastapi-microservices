<script>
import {getBasket, showPrice, updateCartGood} from "@/services/ShopService";

export default {
  name: "CartView",
  methods: {
    showPrice,
    basketGoodDecrement(basketGood){
      if (basketGood.amount <= 1){
        return;
      }
      basketGood.amount -= 1;
      updateCartGood(basketGood.id, basketGood.amount)

    },

     basketGoodIncrement(basketGood){
      basketGood.amount += 1;
      updateCartGood(basketGood.id, basketGood.amount)

    },

  },
  data(){
    return{
        basket: {},
        basketGoods: [],

    }
  },

  mounted() {
    getBasket()
        .then((response) => {
          this.basket = response.data;
          this.basketGoods = response.data.basket_goods;
        })
        .catch((error) => {
          console.error(error)
          this.$router.push({name: "login"})
        })
  },

}
</script>


<template>
 <div class="single-product-area">
        <div class="zigzag-bottom"></div>
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <div class="product-content-right">
                        <div class="woocommerce">
                           <table cellspacing="0" class="shop_table cart">
                                    <thead>
                                        <tr>
                                            <th class="product-remove">&nbsp;</th>
                                            <th class="product-name">Product</th>
                                            <th class="product-price">Price</th>
                                            <th class="product-quantity">Amount</th>
                                            <th class="product-subtotal">Total</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="basketGood in basketGoods" class="cart_item" :key="basketGood">
                                            <td class="product-remove">
                                                <a title="Remove this item" class="remove" href="#">×</a>
                                            </td>

                                            <td class="product-name">
                                                <router-link :to="{name: 'product', params: {id: `${basketGood.good.id}`}}">
                                                  {{ basketGood.good.title }}
                                                </router-link>
                                            </td>

                                            <td class="product-price">
                                                <span class="amount">{{ showPrice(basketGood.good.price, basketGood.good.discount) }} RUB</span>
                                            </td>

                                            <td class="product-quantity">
                                                <div class="quantity buttons_added">
                                                    <input type="button" class="minus" value="-" @click="basketGoodDecrement(basketGood)">
                                                    <input type="number" size="4" class="input-text qty text" title="Qty"
                                                           :value="basketGood.amount" min="1" step="1">
                                                    <input type="button" class="plus" value="+" @click="basketGoodIncrement(basketGood)">
                                                </div>
                                            </td>

                                            <td class="product-subtotal">
                                                <span class="amount">{{ showPrice(basketGood.good.price, basketGood.good.discount) * basketGood.amount }} RUB</span>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="actions" colspan="6">
                                                <button type="button" class="checkout-button button alt wc-forward btn btn-primary">
                                                  Order
                                                </button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>

</style>