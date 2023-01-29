/** @type {import('./$types').PageServerLoad} */
export async function load({ event, fetch }: any) {
    const dishes = await fetch('https://louismeunier.pythonanywhere.com/api/dishes');
    const dishes_json = await dishes.json();
    return dishes_json;
}