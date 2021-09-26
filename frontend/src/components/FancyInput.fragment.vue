<script>
import Axios from "axios";

export default {
    name: "FancyInput",
    data() {
        return {
            input: "",
            output: "",
        };
    },
    methods: {
        async fancify() {
            if (!this.input.trim()) return;

            const res = await Axios.post(`${process.env.VUE_APP_API_ADDRESS}/fancify`, { content: this.input });
            this.output = res.data.result;

            this.$store.commit("addToHistory", { createdAt: Date.now(), input: this.input, output: this.output });
        },
        reset() {
            this.input = this.output = "";
        },
    },
}
</script>

<template>

    <section id="fancy-input">
        <label class="fancy-accent fancy-label">// Very lame.</label>

        <input @click="!!output && reset()" v-model="input" class="fancy-input" placeholder="Boring text goes in here" :readonly="!!output" type="text">

        <a @click="fancify()" class="fancy-button" :disabled="!input.trim()">Fancify</a>

        <label class="fancy-accent fancy-label">// Such fancy.</label>

        <input v-model="output" class="fancy-input" placeholder="Fancy stuff comes out here" readonly style="font-feature-settings: 'salt'" type="text">
    </section>

</template>

<style scoped>

    #fancy-input {
        background-color: #48B3D533;
        margin: 1em -1em;
        padding: 1em;
    }

    .fancy-button:hover {
        background-color: #065F7A;
    }

    .fancy-input {
        background: transparent;
        border: none;
        color: #FFF;
        display: block;
        font-family: "+Jakarta Sans";
        font-size: 2em;
        font-weight: 700;
        width: 100%;
    }

    .fancy-input:focus {
        border: none;
        box-shadow: none;
        outline: none;
    }

    .fancy-label {
        display: block;
        font-weight: 600;
        margin-bottom: 2em;
    }

</style>