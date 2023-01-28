import type { PageLoad } from './$types';
 
export const load = (async ({ event, params }: any) => {
    const response = await event.request(`mcgillMenu.elliottkalt.com/api/dining_halls`);
    return response.json();
}) satisfies PageLoad;