<script>
import Axios from "axios";

export default {
    name: "FancyInput",
    data() {
        return {
            copied: false,
            input: "",
            output: "",
        };
    },
    methods: {
        async copyToClipboard() {
            await navigator.clipboard.writeText(this.output);
            this.copied = true;

            setTimeout(() => this.copied = false, 2000);
        },
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
};
</script>

<template>
  <section id="fancy-input">
    <label class="fancy-accent fancy-label">// Very lame.</label>

    <input
      v-model="input"
      class="fancy-input"
      placeholder="Boring text goes in here"
      :readonly="!!output"
      type="text"
      @click="!!output && reset()"
    >

    <a
      class="fancy-button"
      :disabled="!input.trim()"
      @click="fancify()"
    >Fancify</a>

    <label class="fancy-accent fancy-label">// Such fancy.</label>

    <input
      v-model="output"
      class="fancy-input"
      placeholder="Fancy stuff comes out here"
      readonly
      style="font-feature-settings: 'salt'"
      type="text"
    >

    <a
      class="fancy-button fancy-copy-button"
      :class="{ 'is-done': copied }"
      :disabled="!output"
      @click="copyToClipboard()"
      v-text="copied ? '✓' : 'Copy'"
    />
  </section>
</template>

<style scoped>

    #fancy-input {
        background-color: #48B3D533;
        margin: 1em -1em;
        padding: 1em;
        position: relative;
    }

    .fancy-button:hover {
        background-color: #065F7A;
    }

    .fancy-copy-button {
        bottom: 12px;
        margin: 0;
        min-width: 60px;
        padding: 8px 12px;
        position: absolute;
        right: 12px;
        text-align: center;
    }

    .fancy-copy-button.is-done {
        background-color: #23E279;
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
