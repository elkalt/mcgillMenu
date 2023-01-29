import type { PageLoad } from './$types';
 
export const load = (async () => {
    const response = await fetch(`https://louismeunier.pythonanywhere.com/api/dining_halls`);
    const response_json = await response.json();
    return response_json;
}) satisfies PageLoad;