<script>
import {getGoodsListBySubcategory, getSubcategory, showPrice} from "@/services/ShopService";

export default {
  name: "ShopView",
  data(){
    return{
      subcategoryId: null,
      categoryId: null,
      goods: [],
      subcategory: {},
      category: {}

    }
  },

  mounted() {
    this.categoryId = this.$route.params.category_id;
    this.subcategoryId = this.$route.params.subcategory_id;
     getSubcategory(this.subcategoryId)
        .then((response) => {
          let data = response.data;
          this.subcategory = data
          this.category = data.category;
        })
    getGoodsListBySubcategory(this.subcategoryId)
        .then((response) => {
          this.goods = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
  },

  methods: {
    showPrice

  }

}
</script>

<template>
  <div class="container">
    <div class="product-breadcroumb">
      <router-link :to="{name: 'shop'}">Shop</router-link>
      <router-link :to="{name: 'category', params: {category_id: `${categoryId}`}}">{{ category.title }}</router-link>
      <a class="active-link" href="">{{ subcategory.title }}</a>
    </div>
    <div class="single-product-area">
        <div class="zigzag-bottom"></div>
        <div class="container">
            <div class="row">
                <div class="col-md-3 col-sm-6" v-for="good in goods" v-bind:key="good">
                      <div class="single-shop-product">
                          <div class="product-upper">
                              <img src="img/product-2.jpg" :alt="good.title">
                          </div>
                          <h2><router-link :to="{name: 'product', params: {id: good.id}}">{{ good.title }}</router-link></h2>
                          <div v-if="good.discount" class="product-carousel-price">
                              <ins>{{ showPrice(good.price, good.discount) }}</ins> <del>{{ good.price }}</del>
                          </div>
                         <div v-else class="product-carousel-price">
                              <ins>{{ good.price }}</ins>
                          </div>

                          <div class="product-option-shop">
                              <a class="add_to_cart_button" data-quantity="1" data-product_sku="" data-product_id="70" rel="nofollow" href="/canvas/shop/?add-to-cart=70">Add to cart</a>
                          </div>
                      </div>
                  </div>
            </div>

            <div class="row">
                <div class="col-md-12">
                    <div class="product-pagination text-center">
                        <nav>
                          <ul class="pagination">
                            <li>
                              <a href="#" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                              </a>
                            </li>
                            <li><a href="#">1</a></li>
                            <li><a href="#">2</a></li>
                            <li><a href="#">3</a></li>
                            <li><a href="#">4</a></li>
                            <li><a href="#">5</a></li>
                            <li>
                              <a href="#" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                              </a>
                            </li>
                          </ul>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </div>

</template>

<style>

</style>
