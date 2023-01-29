import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
 
export const load = (async ({ params }: any) => {
    const response = await fetch(`https://louismeunier.pythonanywhere.com/api/dishes/${params.slug}`);
    const response_json = await response.json();
    if (response_json.status === 404) {
        throw error(404, 'Not found');
    }
    return { response_json };
}) satisfies PageLoad;