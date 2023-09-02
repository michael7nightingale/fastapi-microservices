<script>
import {getUser} from "@/services/Auth";
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";

export default {
  name: 'App',
  components: {
    Footer,
    Header
  },
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
 <Header/>
  <div class="site-branding-area">
    <div class="row">
      <div class="logo">
        <h1><a href=""><img  style="width: 100%" :src="'../body.jpg'"></a></h1>
      </div>
    </div>
    </div> <!-- End site branding area -->
    <router-view/>
    <Footer/>
</template>


<style>
</style>
