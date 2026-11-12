# Shopify reads

Every Shopify call in this skill is a read. Use them to check the context the
user gives. Discover fields from the live schema instead of guessing, and
never guess an ID or a handle.

| Need | Source | Use |
| --- | --- | --- |
| Store check | `shop { name primaryDomain { host } }` | Must be YuliSkin on `yuliskin.de`; stop otherwise |
| Target | Product, collection, or article by handle: title, status/published state, `onlineStoreUrl` or handle | Must be published. Link = `https://yuliskin.de/products|collections|blogs/<blog>/<handle>`, no `/en` |
| Fact sources | Product description and metafields, brand site, `Products/<Company>/<Product>/brief.txt` | Record each one under `## Sources` |
| Product photos | The product's featured media URL | Download to `product-photos/` only when the slide shows real products |
| Handle check | `metaobjectByHandle(handle: {type: "slideshow", handle: "<handle>"})` | `null` = free. Otherwise try `-2`, `-3`, … The user creates the `slideshow` metaobject under this handle |
