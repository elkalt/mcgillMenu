/** @type {import('./$types').PageServerLoad} */
export async function load({ event, fetch }: any) {
    const dishes = await fetch('https://louismeunier.pythonanywhere.com/api/dishes');
        // .then((res: { json: () => Response; }) => res.json())
        // .catch((err: any) => console.log(err));
    console.log(dishes);
    return dishes.json();
}