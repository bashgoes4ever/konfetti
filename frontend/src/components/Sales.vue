<template>
    <div>
        <section class="block9"><img src="img/sales/bg.png" alt="" class="block__bg block9__bg"/>
            <div class="container">
                <h1>Акции</h1>
                <div class="block1__descriptor">Офоормление праздников воздушными шарами, <br>декорирование и праздничные товары</div>
            </div>
        </section>
        <section class="block14">
            <div class="container">
                <div class="block14__flex" v-if="items.length != 0">

                    <a href="/"
                       class="block6__item block14__item"
                       v-for="item in items"
                       :key="item.id"
                       :data-title="item.name"
                       :data-text="item.text"
                       :data-image="`http://127.0.0.1:8000/${item.image_thumb}`"
                    >
                        <div class="block2__item__text block6__item__text">
                            <div class="title">{{item.name}}</div>
                            <div class="text">{{trimString(item.text, 145)}}</div>
                            <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
                            <div class="trigger">{{item.trigger}} </div>
                        </div>
                    </a>

                </div>

                <div class="block2-load-wrapp load-wrapp" v-else>
                    <div class="load-3">
                        <div class="line"></div>
                        <div class="line"></div>
                        <div class="line"></div>
                    </div>
                </div>
            </div>
        </section>
        <section class="block12">
            <div class="container">
                <div class="block12__flex">
                    <div class="title">Оформление <br>праздников <br>во Владивостоке</div>
                    <div class="text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla quam velit, vulputate eu pharetra nec, mattis ac neque. Duis vulputate commodo lectus, ac blandit elit tincidunt id. Sed rhoncus, tortor sed eleifend tristique, tortor mauris molestie elit, et lacinia ipsum quam nec dui. <br><br> Quisque nec mauris sit amet elit iaculis pretium sit amet quis magna. Aenean velit odio, elementum in tempus ut, vehicula eu diam. Pellentesque rhoncus aliquam mattis. Ut vulputate eros sed felis sodales nec vulputate justo hendrerit. Vivamus varius pretium ligula, a aliquam odio euismod sit amet. Quisque laoreet sem sit amet orci ullamcorper at ultricies metus viverra. Pellentesque arcu mauris, malesuada quis ornare accumsan, blandit sed diam.</div>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
    import $ from 'jquery'
    export default {
        name: "Sales",
        data: () => ({
            items: []
        }),
        created: function () {
            this.getItems()
        },
        methods: {
            getItems(){
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/sales/',
                    type: 'GET',
                    success: (data) => {
                        this.items = data
                    },
                    error: (err) => {
                        this.items = err
                    }
                })
            },
            trimString(str, max_len) {
                if (str.length < max_len) return str
                let trimmedString = str.substr(0, max_len)
                return trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" "))) + '...'
            }
        }
    }
</script>