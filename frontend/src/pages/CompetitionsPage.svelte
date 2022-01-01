<script lang="ts">
  import { push } from "svelte-spa-router";
  import CompetitionCard from "../components/CompetitionCard.svelte";
  import ScrollableDiv from "../components/ScrollableDiv.svelte";
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
<ScrollableDiv>
  {#each competitions as comp}
    <CompetitionCard competition={comp} />
  {/each}
</ScrollableDiv>

<style>
  h2 {
    color: var(--pal-text-dark);
  }
</style>
