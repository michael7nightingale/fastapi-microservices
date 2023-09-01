<script>
import {getUser} from "@/services/Auth";

export default {
  name: 'App',
  data(){
    return{
        currencies: {
          "RUB": "RUB",
          "USD": "$",
        },
      currentCurrencySign: "RUB",
      currentCurrency: "RUB"
    }
  },
  computed:{
    Year(){
      return new Date().getFullYear().toString();
    },

    User(){
      return getUser();
    }
  },

  methods: {
    currencyClick(currency, sign){
      this.currentCurrency = currency;
      this.currentCurrencySign = sign;
    }
  }
}
</script>


<template>
  <div class="header-area">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <div class="user-menu row">
                        <ul>
                            <li><router-link :to="{name: 'homepage'}"><i class=""></i>Home</router-link></li>
                            <li><router-link :to="{name: 'shop'}"><i class=""></i>Shop</router-link></li>
                            <li><router-link :to="{name: 'product'}"><i class=""></i>Product</router-link></li>
                             <li v-if="User"><a><i class="fa fa-heart"></i> Wishlist</a></li>
                          <li v-if="User"><a><i class="fa fa-user"></i> My Account</a></li>
                            <li v-if="User">
                              <router-link :to="{name: 'cart'}">
                                Cart - <span class="cart-amunt">$100</span> <i class="fa fa-shopping-cart"></i>
                              </router-link></li>
                             <li v-else><router-link :to="{name: 'login'}"><i class="fa fa-user"></i> Login</router-link></li>
                        </ul>
                    </div>
                </div>

                <div class="col-md-4">
                    <div class="header-right">
                        <ul class="list-unstyled list-inline">
                            <li class="dropdown dropdown-small">
                                <a data-toggle="dropdown" data-hover="dropdown" class="dropdown-toggle" href="#"><span class="key">currency :</span><span class="value">{{ currentCurrency }} </span><b class="caret"></b></a>
                                <ul class="dropdown-menu">
                                    <li v-for="(sign, currency) in currencies" v-bind:key="currency" :data-value="sign">
                                      <a @click="currencyClick(currency, sign)" style="user-select: none">{{ currency }}</a>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div> <!-- End header area -->
  <div class="site-branding-area">
    <div class="row">
      <div class="logo">
        <h1><a href=""><img  style="width: 100%" :src="'body.jpg'"></a></h1>
      </div>
    </div>
    </div> <!-- End site branding area -->
    <router-view/>

    <div class="footer-bottom-area">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <div class="copyright">
                        <p>&copy; {{ Year }} All Rights Reserved.</p>
                    </div>
                </div>
            </div>
        </div>
    </div> <!-- End footer bottom area -->
</template>


<style>
@import "assets/css/bootstrap.min.css";
@import "assets/css/font-awesome.min.css";
@import "assets/css/owl.carousel.css";
@import "assets/css/style.css";
@import "assets/css/responsive.css";
</style>
