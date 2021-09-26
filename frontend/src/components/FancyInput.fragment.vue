<script>
export default {
    name: "FancyInput",
}
</script>

<template>

    <section id="fancy-input">
        <label class="fancy-accent fancy-label">// Very lame.</label>

        <input class="fancy-input" placeholder="Boring text goes in here" type="text">

        <a class="fancy-button">Fancify</a>

        <label class="fancy-accent fancy-label">// Such fancy.</label>

        <input class="fancy-input" placeholder="Fancy stuff comes out here" readonly style="font-feature-settings: 'salt'" type="text">
    </section>

</template>

<style scoped>

    #fancy-input {
        background-color: #48B3D533;
        margin: 1em -1em;
        padding: 1em;
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