<script lang="ts">
let num = 0
function ButtonClicked() {
    num++;
}
</script>

<main>
    <button on:click={ButtonClicked}>{num}</button>
</main>