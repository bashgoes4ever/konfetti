<template>
    <div>
        <section class="block9"><img src="img/ideas/bg.png" alt="" class="block__bg block9__bg"/>
            <div class="container">
                <h1>Наши идеи</h1>
                <div class="block1__descriptor">Мы всегда рады поделиться <br>своими свежими идеями</div>
            </div>
        </section>
        <section class="block13">
            <div class="container">
                <div class="block6__flex" v-if="ideas.length != 0">

                    <a href="/"
                       class="block6__item"
                       v-for="idea in ideas"
                       :key="idea.id"
                       :data-title="idea.name"
                       :data-text="idea.text"
                       :data-image="`http://127.0.0.1:8000/${idea.image_thumb}`"
                    >
                        <div class="block2__item__text block6__item__text">
                            <div class="title">{{idea.name}}</div>
                            <div class="text">{{trimString(idea.text, 145)}}</div>
                            <div class="link">Подробнее <img src='img/icons/arrow.png' /></div>
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
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Ideas",
        data: () => ({
            ideas: []
        }),
        created: function () {
            this.getIdeas()
        },
        methods: {
            getIdeas() {
                $.ajax({
                    url: 'http://127.0.0.1:8000/api/v1/ideas/',
                    type: 'GET',
                    success: (data) => {
                        this.ideas = data
                    },
                    error: (err) => {
                        this.ideas = err
                    }
                })
            },
            trimString(str, max_len) {
                if (str.length < max_len) return str
                let trimmedString = str.substr(0, max_len);
                return trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" "))) + '...'
            }
        }
    }
</script>

<style scoped>

</style>