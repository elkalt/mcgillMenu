import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
 
export const load = (async ({ event, params }: any) => {
    const response = await event.request(`mcgillMenu.elliottkalt.com/api/dishes/${params.slug}`);
    if (response.status === 404) {
        throw error(404, 'Not found');
    }
    return response.json();
}) satisfies PageLoad;