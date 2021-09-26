<script>
export default {
    name: "FancyHistory",
}
</script>

<template>

    <section id="fancy-history">
        <article class="fancy-history">
            <label class="fancy-accent fancy-meta">25.09.2021 11:01</label>
            <div style="align-items: center; display: flex; flex-wrap: wrap">
                <div class="fancy-input">Gentleman Archibald</div>
                <div class="fancy-arrow">→</div>
                <div class="fancy-output">der klassische Reiskocher</div>
            </div>
        </article>

        <article class="fancy-history">
            <label class="fancy-accent fancy-meta">26.09.2021 14:27</label>
            <div style="align-items: center; display: flex; flex-wrap: wrap">
                <div class="fancy-input">oRRUcuvc</div>
                <div class="fancy-arrow">→</div>
                <div class="fancy-output">der vorsintflutliche Verdauungstrakt</div>
            </div>
        </article>
    </section>

</template>

<style scoped>

    #fancy-history {
        margin: 1em -1em;
    }

    .fancy-arrow,
    .fancy-input,
    .fancy-output {
        color: #FFFFFF80;
        font-family: "+Jakarta Sans";
        font-weight: 500;
        line-height: 1;
    }

    .fancy-arrow {
        display: none;
        font-size: 1.5em;
        margin: 0 .5em 4px;
    }

    .fancy-history {
        background-color: #48B3D533;
        padding: 1em;
    }

    .fancy-history ~ .fancy-history {
        margin-top: 1em;
    }

    .fancy-input {
        font-size: 1.25em;
    }

    .fancy-meta {
        display: block;
        font-size: .85em;
        font-weight: 400;
        margin-bottom: .75em;
    }

    .fancy-output {
        color: #FFF;
        font-feature-settings: "salt";
        font-size: 1.5em;
        font-weight: 600;
        margin-top: .25em;
        width: 100%;
    }

    @media screen and (min-width: 800px) {
        .fancy-arrow {
            display: block;
        }

        .fancy-input {
            font-size: 1.5em;
        }

        .fancy-output {
            margin: 0;
            width: unset;
        }
    }

</style>