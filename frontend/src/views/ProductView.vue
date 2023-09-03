<script>
import {getGood, getGoodDescriptionTags} from "@/services/ShopService";
import {getUser} from "@/services/Auth";

export default {
  name: "ProductView",
  data(){
    return{
      goodId: null,
      good: {},
      category: {},
      subcategory: {},
      descriptionTags: {},
      amount: 1,

    }
  },

  computed: {
    User(){
      return getUser();
    }
  },

  mounted(){
    this.goodId = this.$route.params.id;
    getGood(this.goodId)
        .then((response) => {
            let data = response.data;
            this.good = data;
            this.category = data.category;
            this.subcategory = data.subcategory;
        })

    getGoodDescriptionTags(this.goodId)
        .then((response) => {
          this.descriptionTags = response.data;
        })
  },

   methods: {
    showPrice(price, discount){
      return price * (1 - (discount / 100))
    },

     amountInput(value){
      this.amount = value
    },

     addCartClick(){
      if (!this.User){
          this.$router.push({name: "login"})
      }
      else{
          this.$router.push({name: "cart"})
      }
     },

  }

}
</script>

<template>
<div class="single-product-area">
        <div class="zigzag-bottom"></div>
        <div class="container">
          <div>
            <div class="">
              <div class="product-breadcroumb">
                <router-link :to="{name: 'shop'}">Shop</router-link>
                <router-link :to="{name: 'category', params: {category_id: `${category.id}`}}">{{ category.title }}</router-link>
                <router-link
                    :to="{name: 'subcategory', params: {category_id: `${category.id}`, subcategory_id: `${subcategory.id}`}}"
                >{{ subcategory.title }}</router-link>
                <a class="active-link" href="">{{ good.title }}</a>
              </div>
              <div class="row">
                <div class="col-sm-6">
                  <div class="product-images">
                    <div class="product-main-img">
                      <img src="img/product-2.jpg" alt="">
                    </div>
                    <div class="product-gallery">
                      <img src="img/product-thumb-1.jpg" alt="">
                      <img src="img/product-thumb-2.jpg" alt="">
                      <img src="img/product-thumb-3.jpg" alt="">
                    </div>
                  </div>
                </div>
                <div class="col-sm-6">
                  <div class="product-inner">
                    <h2 class="product-name">{{ good.title }}</h2>
                    <div v-if="good.discount" class="product-carousel-price">
                      <ins>{{ showPrice(good.price, good.discount) }}</ins> <del>{{ good.price }}</del>
                    </div>
                    <div v-else class="product-carousel-price">
                      <ins>{{ good.price }}</ins>
                    </div>
                    <form action="" class="cart">
                      <div class="quantity">
                        <input type="number" size="4" class="input-text qty text" :value="amount" min="1" step="1" @input="amountInput($event.target.value)">
                      </div>
                      <button class="add_to_cart_button" type="button" @click="addCartClick">Add to cart</button>
                    </form>
                    <div class="product-inner-category">
                      <p>Category: <a href="">Summer</a>. Tags: <a href="">awesome</a>, <a href="">best</a>, <a href="">sale</a>, <a href="">shoes</a>. </p>
                    </div>
                    <div role="tabpanel">
                      <ul class="product-tab" role="tablist">
                        <li role="presentation" class="active"><a href="#description" aria-controls="description" role="tab" data-toggle="tab">Description</a></li>
                        <li role="presentation"><a href="#specifications" aria-controls="specifications" role="tab" data-toggle="tab">Specifications</a></li>
                        <li role="presentation"><a href="#reviews" aria-controls="reviews" role="tab" data-toggle="tab">Reviews</a></li>
                      </ul>
                      <div class="tab-content">
                        <div role="tabpanel" class="tab-pane fade in active" id="description">
                          <h2>Product Description</h2>
                          <p>{{ good.description }}</p>
                        </div>
                         <div role="tabpanel" class="tab-pane fade in" id="specifications">
                          <p
                              v-for="descriptionTag in descriptionTags"
                              :key="descriptionTag"
                          >
                          {{ `${descriptionTag.tag}: ${descriptionTag.text}` }}
                          </p>
                        </div>
                        <div role="tabpanel" class="tab-pane fade" id="reviews">
                          <h2>Reviews</h2>
                          <div class="submit-review">
                            <p><label for="name">Name</label> <input name="name" type="text"></p>
                            <p><label for="email">Email</label> <input name="email" type="email"></p>
                            <div class="rating-chooser">
                              <p>Your rating</p>
                              <div class="rating-wrap-post">
                                <i class="fa fa-star"></i>
                                <i class="fa fa-star"></i>
                                <i class="fa fa-star"></i>
                                <i class="fa fa-star"></i>
                                <i class="fa fa-star"></i>
                              </div>
                            </div>
                            <p><label for="review">Your review</label> <textarea name="review" id="" cols="30" rows="10"></textarea></p>
                            <p><input type="submit" value="Submit"></p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
            </div>
        </div>
</template>

<style scoped>

</style>