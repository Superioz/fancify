<script>
import FancyHistory from "@/components/FancyHistory.fragment.vue";
import FancyInput from "@/components/FancyInput.fragment.vue";

export default {
    components: {
        FancyHistory,
        FancyInput,
    },
}
</script>

<template>

    <div id="app">
        <img class="fancy-logo" height="32" src="./assets/logo-new.png">

        <div class="fancy-accent">Fancify your sh*t here ↴</div>

        <fancy-input />

        <div class="fancy-accent" style="margin-top: 4em">Your latest fancifies ↴</div>

        <fancy-history />
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
        padding: 1em;
    }

    .fancy-accent {
        color: #48B3D5;
    }

    .fancy-divider {
        background-size: 12px 21px;
        background-image: url("~@/assets/slash.png");
        background-repeat: repeat-x;
        height: 12px;
        width: 100%;
    }

    .fancy-logo {
        margin: 3em 0 2em 0;
    }

</style>