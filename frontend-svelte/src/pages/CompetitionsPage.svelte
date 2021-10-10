<script lang="ts">
  import { push } from "svelte-spa-router";

  import { getAllCompetitions } from "../services/comps";
  import type { ICompetition } from "../types";

  let competitions: ICompetition[] = [];
  getAllCompetitions().then((comps) => {
    competitions = comps;
  });

  function handleClick(comp: number) {
    push(`/comps/${comp}`);
  }
</script>

<h2>Current Members</h2>
<div>
  {#each competitions as comp}
    <div
      class="row"
      on:click={() => {
        handleClick(comp.competitionId);
      }}
    >
      <p class="col1 item">{comp.competitionId}</p>
      <ul class="col2 item">
        {#each comp.allowedStyles as allowedStyle}
          <li>{allowedStyle}</li>
        {/each}
      </ul>
      <p class="col3 item">{comp.description}</p>
    </div>
  {/each}
</div>

<style>
  h2 {
    color: var(--pal-text-dark);
  }
  img {
    width: calc(var(--spacing) * 15);
    height: calc(var(--spacing) * 15);
    border-radius: 50%;
  }
  p {
    font-size: 1rem;
  }
  .row {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    justify-items: center;
    margin: calc(var(--spacing) * 2);
    /* border: 1px solid salmon; */
    border-radius: var(--spacing);
    box-shadow: 2px 2px 3px 0px var(--pal-text-soft),
      3px 3px 5px 0px var(--pal-text-soft);
    cursor: pointer;
  }
  .item {
    justify-self: center;
    align-self: center;
    margin: calc(var(--spacing) * 2);
  }
  .col2::before {
    content: "Allowed Styles";
    display: flex;
    align-items: center;
    justify-content: center;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
  .col3::before {
    content: "Closing Date";
    display: flex;
    align-items: center;
    justify-content: center;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
</style>
