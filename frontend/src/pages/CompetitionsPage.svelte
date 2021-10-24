<script lang="ts">
  import { push } from "svelte-spa-router";
  import CompetitionCard from "../components/CompetitionCard.svelte";
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

<h2>Competitions</h2>
<div>
  {#each competitions as comp}
    <CompetitionCard competition={comp} />
  {/each}
</div>

<style>
  h2 {
    color: var(--pal-text-dark);
  }
</style>
