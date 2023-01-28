/** @type {import('./$types').PageServerLoad} */
export async function load({ event, fetch }: any) {
    const dishes = await event.request('mcgillMenu.elliottkalt.com/api/dishes/').then((res: { json: () => Response; }) => res.json());
    return dishes.json();
}