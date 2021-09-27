<script>
import FancyHistory from "@/components/FancyHistory.fragment.vue";
import FancyInput from "@/components/FancyInput.fragment.vue";

export default {
    components: {
        FancyHistory,
        FancyInput,
    },
    methods: {
        hasHistory() {
            return this.$store.state.history.filter(entry => !!entry).length > 0;
        },
    },
}
</script>

<template>

    <div id="app">
        <div :class="{ 'fancy-center': !hasHistory() }">
            <img class="fancy-logo" height="32" src="./assets/logo.png">

            <div class="fancy-accent">Fancify your sh*t here ↴</div>

            <fancy-input />
        </div>

        <template v-if="hasHistory()">
            <div class="fancy-accent" style="margin-top: 4em">Your latest fancifies ↴</div>
            <fancy-history />
        </template>
    </div>

</template>

<style>

    @import url("./assets/pjs.css");

    *, *::after, *::before {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        background-color: #0C1419;
        font-family: "JetBrains Mono", monospace;
        font-size: 14px;
    }

    #app {
        margin: 0 auto;
        max-width: 800px;
        min-height: 100vh;
        padding: 1em;
        position: relative;
    }

    .fancy-accent {
        color: #48B3D5;
    }

    .fancy-button {
        background-color: #48B3D5;
        color: #FFF;
        cursor: pointer;
        display: block;
        font-weight: 700;
        letter-spacing: .5px;
        margin: 1em -1em;
        padding: 1em;
        text-align: center;
        text-transform: uppercase;
        user-select: none;
    }

    .fancy-button[disabled] {
        opacity: .25;
        pointer-events: none;
    }

    .fancy-logo {
        margin: 3em 0 2em 0;
    }

    @media screen and (min-width: 860px) {
        .fancy-center {
            margin-left: -1em;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 100%;
        }

        .fancy-center .fancy-logo {
            margin-top: 0;
        }

        .fancy-center section {
            margin-bottom: 0 !important;
        }
    }

</style>