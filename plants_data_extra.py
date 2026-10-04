"""
NurseryIQ extra seed data: 300 more plants (50 per primary category).

Same line format and codes as plants_data.py:
name | scientific name | emoji | tags (first = primary category) | sun | water |
environments | level | temperature | soil | best planting seasons | description | care

Photos are looked up from the scientific name, so keep that spelling accurate.
"""

_RAW_EXTRA = """
Swiss Cheese Plant|Monstera adansonii|🌿|Indoor|m|m|i|b|18-30°C|Airy, well-draining potting mix|s,m|Vining plant with naturally holey leaves.|Give a moss pole and bright indirect light; water when the top soil dries.
Split-Leaf Philodendron|Thaumatophyllum bipinnatifidum|🌿|Indoor|m|m|i|b|18-30°C|Rich, well-draining potting mix|s,m|Large, deeply lobed leaves on a bushy plant.|Allow room to spread and water when the top soil dries.
Pink Princess Philodendron|Philodendron erubescens|🌿|Indoor|m|m|i|e|18-30°C|Airy, well-draining mix|s,m|Dark leaves splashed with pink variegation.|Give bright indirect light to keep the pink colour.
Philodendron Gloriosum|Philodendron gloriosum|🍃|Indoor|m|m|i|e|20-30°C|Airy, chunky potting mix|s,m|Creeping plant with large velvety heart-shaped leaves.|Let the rhizome creep on the surface and keep humidity high.
Satin Pothos|Scindapsus pictus|🍃|Indoor|m|m|i|b|18-30°C|Well-draining potting mix|s,m,w|Silver-splashed velvety leaves on trailing vines.|Water when the top soil is dry and avoid direct sun.
Alocasia Polly|Alocasia x amazonica|🌿|Indoor|m|m|i|e|18-30°C|Rich, well-draining mix|s,m|Dark arrow-shaped leaves with bold white veins.|Keep soil lightly moist, humid and out of cold drafts.
Alocasia Zebrina|Alocasia zebrina|🌿|Indoor|m|m|i|e|20-30°C|Rich, well-draining mix|s,m|Zebra-striped stems topped with arrow-shaped leaves.|Provide humidity and bright indirect light.
Guzmania|Guzmania lingulata|🌺|Indoor|m|m|i|b|18-28°C|Bromeliad or orchid mix|s,m|Bromeliad with a long-lasting colourful bract.|Keep water in the central cup and refresh it often.
Silver Vase Plant|Aechmea fasciata|🌸|Indoor|m|m|i|b|18-30°C|Bromeliad or orchid mix|s,m|Silvery banded leaves around a pink flower spike.|Water the central cup and avoid soggy soil.
Air Plant|Tillandsia ionantha|🪴|Indoor|m|l|i,b|b|15-30°C|No soil needed|s,m,w|Soil-free plant that absorbs moisture through its leaves.|Soak weekly for 20 minutes and dry it completely afterwards.
Anthurium Clarinervium|Anthurium clarinervium|🍃|Indoor|m|m|i|e|18-28°C|Airy, chunky aroid mix|s,m|Velvety heart-shaped leaves with white veins.|Use a chunky mix and keep humidity high.
Wax Plant|Hoya carnosa|🌸|Indoor|h|l|i,b|b|15-30°C|Light, well-draining mix|s,m|Waxy leaves and fragrant star-shaped flower clusters.|Water when dry and keep old flower stalks for new blooms.
Sweetheart Hoya|Hoya kerrii|💚|Indoor|h|l|i,b|b|18-30°C|Gritty, well-draining mix|s,m|Heart-shaped succulent leaves on slow-growing vines.|Water sparingly and give bright light.
Lipstick Plant|Aeschynanthus radicans|🌺|Indoor|m|m|i,b|e|18-28°C|Light, airy potting mix|s,m|Trailing vines with red tubular flowers.|Keep humid, water when the top soil dries and avoid direct sun.
Goldfish Plant|Nematanthus gregarius|🐠|Indoor|m|m|i,b|e|18-27°C|Light, airy potting mix|s,m|Glossy leaves and small orange goldfish-shaped flowers.|Keep soil lightly moist and avoid overwatering.
Rattlesnake Plant|Goeppertia insignis|🍃|Indoor|l|m|i|e|18-27°C|Rich, well-draining mix|m,w|Long wavy leaves with dark spots.|Use filtered water and keep the air humid.
Rose-Painted Calathea|Calathea roseopicta|🍃|Indoor|l|m|i|e|18-27°C|Rich, well-draining mix|m,w|Round leaves painted with pink and green.|Keep soil lightly moist and avoid direct sun.
Stromanthe Triostar|Stromanthe sanguinea|🌈|Indoor|m|m|i|e|18-28°C|Rich, well-draining mix|m,w|Pink, cream and green leaves with maroon undersides.|Keep humid and use filtered water.
Ctenanthe|Ctenanthe setosa|🍃|Indoor|l|m|i|e|18-27°C|Rich, well-draining mix|m,w|Feather-patterned leaves that fold at night.|Keep soil lightly moist and avoid dry air.
Bamboo Palm|Chamaedorea seifrizii|🌴|Indoor|m|m|i,b|b|18-30°C|Well-draining potting mix|s,m,w|Clumping palm with slim, reed-like stems.|Keep soil lightly moist and out of direct sun.
Lady Palm|Rhapis excelsa|🌴|Indoor|m|m|i,b|b|10-30°C|Rich, well-draining potting mix|s,m|Fan-shaped leaves on slender, bamboo-like stems.|Water when the top soil dries and avoid harsh sun.
Majesty Palm|Ravenea rivularis|🌴|Indoor|h|h|i,b|e|18-32°C|Rich, well-draining potting mix|s,m|Graceful palm that likes steady moisture and bright light.|Keep soil evenly moist and provide humidity.
Cat Palm|Chamaedorea cataractarum|🌴|Indoor|m|m|i,b|b|18-30°C|Rich, well-draining potting mix|s,m|Dense, glossy palm that tolerates some low light.|Keep soil lightly moist and mist occasionally.
Fishtail Palm|Caryota mitis|🌴|Indoor|m|m|i,o,b|b|20-35°C|Rich, well-draining potting mix|s,m|Clumping palm with fishtail-shaped leaflets.|Water regularly; the fruit is irritating, so keep it out of reach.
Umbrella Plant|Schefflera arboricola|🌿|Indoor|m|m|i,b|b|15-30°C|Well-draining potting mix|s,m,w|Shiny, umbrella-like leaf clusters that tolerate trimming.|Water when the top soil dries and prune to shape.
Ming Aralia|Polyscias fruticosa|🌿|Indoor|m|m|i,b|e|18-30°C|Well-draining potting mix|s,m|Lacy, fine leaves with a bonsai-like look.|Keep soil lightly moist and avoid cold drafts.
Corn Plant|Dracaena fragrans|🌿|Indoor|l|m|i|b|18-30°C|Well-draining potting mix|s,m,w|Arching, corn-like leaves with a central stripe.|Water lightly; fluoride in tap water can brown the tips.
Gold Dust Dracaena|Dracaena surculosa|🍃|Indoor|l|m|i|b|18-30°C|Well-draining potting mix|s,m,w|Dark leaves speckled with cream spots.|Keep soil lightly moist and out of direct sun.
Kangaroo Fern|Microsorum diversifolium|🌿|Indoor|m|m|i,b|b|10-28°C|Moist, well-draining mix|m,w|Tough, glossy fern with leathery fronds.|Keep soil lightly moist and avoid harsh sun.
Staghorn Fern|Platycerium bifurcatum|🌿|Indoor|m|m|i,b|e|15-28°C|Mounted on bark or moss|m,w|Antler-shaped fronds usually grown mounted.|Soak the mount weekly and mist the fronds.
Maidenhair Fern|Adiantum raddianum|🌿|Indoor|l|h|i|e|15-25°C|Moist, humus-rich mix|m,w|Delicate fan-shaped fronds on dark stems.|Never let it dry out and keep the air humid.
Rabbit's Foot Fern|Davallia fejeensis|🌿|Indoor|m|m|i,b|b|15-28°C|Light, airy mix|m,w|Furry rhizomes creep over the pot edge.|Keep soil lightly moist and do not bury the rhizomes.
Button Fern|Pellaea rotundifolia|🌿|Indoor|m|m|i,b|b|10-26°C|Light, well-draining mix|m,w|Small round leaflets on arching fronds.|Water when the top soil dries and avoid soggy soil.
Asparagus Fern|Asparagus setaceus|🌿|Indoor|m|m|i,b|b|15-30°C|Well-draining potting mix|s,m,w|Feathery foliage that adds softness to arrangements.|Water regularly; the berries are toxic if eaten.
Sword Fern|Nephrolepis cordifolia|🌿|Indoor|m|m|i,o,b|b|15-30°C|Moist, well-draining mix|m,w|Tough, upright fern for shady spots.|Keep soil lightly moist and give partial shade.
Bunny Ears Cactus|Opuntia microdasys|🌵|Indoor|h|l|i,b|b|15-35°C|Gritty cactus mix|s,w|Paddle-shaped pads with tiny glochids; handle carefully.|Water rarely and give full sun.
Golden Barrel Cactus|Echinocactus grusonii|🌵|Indoor|h|l|i,o,b|b|15-38°C|Gritty cactus mix|s,w|Round, golden-spined cactus that grows slowly.|Water rarely and give maximum light.
Old Lady Cactus|Mammillaria hahniana|🌵|Indoor|h|l|i,b|b|15-35°C|Gritty cactus mix|s,w|Small cactus covered in white hairs with pink flower rings.|Water only when dry and give bright light.
Moon Cactus|Gymnocalycium mihanovichii|🌵|Indoor|m|l|i,b|b|18-32°C|Gritty cactus mix|s,w|Colourful grafted cactus in red, pink or orange.|Give bright light without harsh sun and water sparingly.
Bishop's Cap Cactus|Astrophytum myriostigma|🌵|Indoor|h|l|i,b|b|15-35°C|Gritty cactus mix|s,w|Star-shaped, spineless cactus with a speckled surface.|Water rarely and give bright light.
Peanut Cactus|Echinopsis chamaecereus|🌵|Indoor|h|l|i,b|b|10-32°C|Gritty cactus mix|s,w|Clustering finger-like stems with bright orange flowers.|Water lightly and give bright light.
Fairy Castle Cactus|Acanthocereus tetragonus|🌵|Indoor|h|l|i,b|b|15-35°C|Gritty cactus mix|s,w|Branching, castle-like columns that suit small pots.|Water when dry and give bright light.
Hens and Chicks|Sempervivum tectorum|🪴|Indoor|h|l|i,o,b|b|5-30°C|Gritty succulent mix|s,w|Rosette succulent that spreads by small offsets.|Water sparingly and give full sun.
Panda Plant|Kalanchoe tomentosa|🐼|Indoor|h|l|i,b|b|15-30°C|Gritty succulent mix|s,w|Fuzzy grey leaves with brown-tipped edges.|Water only when dry and avoid wetting the leaves.
Living Stones|Lithops salicola|🪨|Indoor|h|l|i,b|e|15-30°C|Very gritty mineral mix|s,w|Stone-like succulent that blends in with pebbles.|Water only when new leaves emerge in the growing season.
Lace Aloe|Aristaloe aristata|🪴|Indoor|m|l|i,b|b|10-30°C|Gritty succulent mix|s,w|Small rosette with soft white spines and orange flowers.|Water when dry and give bright light.
Gasteria|Gasteria carinata|🪴|Indoor|m|l|i,b|b|15-30°C|Gritty succulent mix|s,m,w|Tough, tongue-like leaves that tolerate lower light.|Water when dry and avoid direct midday sun.
Pencil Cactus|Euphorbia tirucalli|🌵|Indoor|h|l|i,o,b|b|18-38°C|Gritty, well-draining mix|s,m,w|Slim pencil-like stems; the milky sap is irritating.|Wear gloves when pruning and water sparingly.
Pink Quill|Tillandsia cyanea|🌸|Indoor|m|m|i|b|18-30°C|Bromeliad mix or mounted|s,m|Air plant with a flat pink bract and violet flowers.|Mist often and keep the air humid.
Ric Rac Cactus|Disocactus anguliger|🌵|Indoor|m|m|i,b|b|15-30°C|Light, airy cactus mix|s,m|Zigzag trailing stems with fragrant blooms.|Water when the top soil dries and give bright indirect light.
Bird of Paradise|Strelitzia reginae|🦜|Flowering|h|m|o,b|e|15-35°C|Rich, well-draining soil|s,m|Orange and blue crane-like flowers on a bold plant.|Give sun and space; it blooms after a few years.
Gloxinia|Sinningia speciosa|🌺|Flowering|m|m|i|e|18-26°C|Light, airy mix|s,m|Velvety bell-shaped flowers in rich colours.|Water from below and avoid wetting the leaves.
Azalea|Rhododendron simsii|🌸|Flowering|m|m|o,b|e|10-25°C|Acidic, humus-rich soil|w|Masses of bright flowers on a compact shrub.|Use acidic soil, keep it moist and avoid hot sun.
Rain Lily|Zephyranthes candida|🌷|Flowering|h|m|o,b|b|18-35°C|Well-draining loamy soil|m|Crocus-like white flowers that burst open after rain.|Plant bulbs in the monsoon and water regularly.
Spider Lily|Hymenocallis littoralis|🌼|Flowering|h|m|o,b|b|20-35°C|Rich, moist loamy soil|m|Fragrant white spidery flowers on a bulb plant.|Keep soil moist and feed during the growing season.
Crinum Lily|Crinum asiaticum|🌼|Flowering|m|m|o|b|20-35°C|Rich, moist loamy soil|m|Large bulb with fragrant white flower clusters.|Water regularly; the bulbs are toxic if eaten.
Dendrobium Orchid|Dendrobium nobile|🌸|Flowering|m|m|i,o,b|e|15-30°C|Bark or coconut-husk mix|m,w|Cane orchid with clusters of showy flowers.|Water well in growth and reduce in the cool, dry season.
Vanda Orchid|Vanda tessellata|🌸|Flowering|h|m|o,b|e|20-35°C|Hang in a slatted basket|s,m|Epiphytic orchid grown with bare roots in the air.|Water and mist often and give bright light.
Cattleya Orchid|Cattleya labiata|🌸|Flowering|m|m|i,b|e|15-30°C|Bark orchid mix|m,w|Large, fragrant ruffled flowers.|Let the mix dry slightly between waterings.
Dancing Lady Orchid|Oncidium sphacelatum|🌼|Flowering|m|m|i,b|e|15-30°C|Bark orchid mix|m,w|Sprays of small yellow and brown flowers.|Water when the mix is nearly dry and give bright light.
Ginger Lily|Hedychium coronarium|🌼|Flowering|m|h|o|b|18-35°C|Rich, moist loamy soil|m|Fragrant white butterfly-like flowers on tall stems.|Keep soil moist and cut old stems after flowering.
Torch Ginger|Etlingera elatior|🌺|Flowering|m|h|o|e|22-35°C|Rich, moist soil|m|Tall plant with spectacular red torch-shaped flowers.|Give humidity, regular water and room to spread.
Red Ginger|Alpinia purpurata|🌺|Flowering|m|h|o|b|20-35°C|Rich, moist soil|s,m|Long-lasting red bracts on a tropical clump.|Keep soil moist and protect from strong wind.
Shell Ginger|Alpinia zerumbet|🌸|Flowering|m|m|o|b|20-35°C|Rich, moist soil|m|Clumping plant with variegated leaves and shell-like flowers.|Water regularly and give partial shade.
Plumbago|Plumbago auriculata|💙|Flowering|h|m|o,b|b|15-35°C|Well-draining loamy soil|s,m|Sprawling shrub with pale blue flower clusters.|Water regularly and prune after flowering.
Bleeding Heart Vine|Clerodendrum thomsoniae|❤️|Flowering|m|m|o,b|b|18-32°C|Rich, well-draining soil|s,m|Climber with white calyces and crimson flowers.|Support the vines and keep soil moist.
Yesterday-Today-and-Tomorrow|Brunfelsia pauciflora|💜|Flowering|m|m|o,b|b|15-32°C|Acidic, well-draining soil|s,m|Flowers change from purple to white over three days.|Keep soil acidic and moist; all parts are toxic.
Impatiens|Impatiens walleriana|🌸|Flowering|l|m|o,b|b|15-30°C|Rich, moist, well-draining soil|m,w|Free-flowering shade plant in many bright colours.|Keep soil moist and shade from hot sun.
Carnation|Dianthus caryophyllus|🌸|Flowering|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Ruffled, long-lasting fragrant flowers.|Water at the base and remove faded flowers.
Sweet William|Dianthus barbatus|🌸|Flowering|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Dense clusters of small, spicy-scented flowers.|Sow in cool weather and deadhead for more blooms.
Delphinium|Delphinium elatum|💙|Flowering|h|m|o|e|10-25°C|Rich, well-draining soil|w|Tall spikes of blue flowers for the cool season.|Stake tall stems and water regularly; toxic if eaten.
Hollyhock|Alcea rosea|🌸|Flowering|h|m|o|b|10-28°C|Rich, well-draining soil|w|Towering spikes of large, saucer-like flowers.|Stake the plants and water deeply.
Sweet Pea|Lathyrus odoratus|🌸|Flowering|h|m|o,b|b|10-22°C|Rich, well-draining soil|w|Fragrant ruffled flowers on a climbing annual.|Provide a trellis and pick often; seeds are toxic.
Nasturtium|Tropaeolum majus|🌼|Flowering|h|m|o,b|b|10-28°C|Poor to average, well-draining soil|w|Easy trailing plant with edible peppery flowers.|Do not over-fertilize or you get leaves not flowers.
Cockscomb|Celosia argentea|🌺|Flowering|h|m|o,b|b|18-35°C|Well-draining loamy soil|s,m|Velvety, brightly coloured plume or crest flowers.|Water regularly and give full sun.
Four O'Clock|Mirabilis jalapa|🌸|Flowering|h|m|o,b|b|18-35°C|Well-draining soil|s,m|Fragrant flowers that open in the late afternoon.|Easy to grow; the seeds and roots are toxic.
Morning Glory|Ipomoea purpurea|💜|Flowering|h|m|o,b|b|18-35°C|Well-draining soil|s,m|Fast climber with trumpet flowers that open at dawn.|Provide a trellis; seeds are toxic if eaten.
Moonflower|Ipomoea alba|🌙|Flowering|h|m|o,b|b|18-35°C|Well-draining soil|s,m|Large white fragrant flowers that open at dusk.|Give a strong support and water regularly.
Cypress Vine|Ipomoea quamoclit|🌺|Flowering|h|m|o,b|b|18-35°C|Well-draining soil|s,m|Delicate feathery climber with small red star flowers.|Provide a thin trellis and full sun.
Verbena|Verbena x hybrida|🌸|Flowering|h|m|o,b|b|10-30°C|Light, well-draining soil|w|Clusters of small flowers on a spreading plant.|Water at the base and deadhead often.
Lobelia|Lobelia erinus|💙|Flowering|m|m|o,b|b|10-25°C|Rich, moist, well-draining soil|w|Tiny blue flowers that spill over pots and baskets.|Keep soil moist and avoid hot afternoon sun.
Sweet Alyssum|Lobularia maritima|🤍|Flowering|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Low carpet of honey-scented white flowers.|Trim back after flowering for a second flush.
Mealycup Sage|Salvia farinacea|💙|Flowering|h|l|o,b|b|15-35°C|Well-draining soil|s,m,w|Spikes of blue flowers that attract bees.|Tolerates dry spells and blooms for months.
Torenia|Torenia fournieri|💜|Flowering|m|m|o,b|b|15-30°C|Rich, moist, well-draining soil|m,w|Wishbone-like flowers that thrive in partial shade.|Keep soil moist and shade from hot sun.
Nemesia|Nemesia strumosa|🌸|Flowering|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Compact plant covered in small, colourful flowers.|Water regularly and trim after the first flush.
Calibrachoa|Calibrachoa x hybrida|🌸|Flowering|h|m|o,b|b|10-28°C|Acidic, well-draining potting mix|w|Mini-petunia flowers in hanging baskets.|Feed regularly and water when the top soil dries.
Cineraria|Pericallis x hybrida|🌸|Flowering|m|m|o,b|b|10-22°C|Rich, well-draining soil|w|Dense daisy-like flowers for cool-season colour.|Keep soil moist and protect from heat.
Corn Poppy|Papaver rhoeas|❤️|Flowering|h|l|o|b|10-25°C|Light, well-draining soil|w|Delicate red flowers that self-seed readily.|Sow directly in cool weather; avoid transplanting.
California Poppy|Eschscholzia californica|🧡|Flowering|h|l|o,b|b|10-28°C|Light, sandy soil|w|Silky orange flowers that open in the sun.|Sow in place and water lightly.
Cornflower|Centaurea cyanus|💙|Flowering|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Bright blue fringed flowers on slim stems.|Sow in cool weather and deadhead to prolong blooms.
Blanket Flower|Gaillardia pulchella|🌼|Flowering|h|l|o,b|b|15-35°C|Light, well-draining soil|s,m,w|Daisy-like flowers in red and yellow that handle heat.|Tolerates drought and blooms for months.
Tickseed|Coreopsis tinctoria|🌼|Flowering|h|l|o,b|b|10-30°C|Light, well-draining soil|m,w|Golden-yellow flowers with maroon centres.|Water lightly and deadhead often.
Black-Eyed Susan|Rudbeckia hirta|🌻|Flowering|h|m|o|b|10-30°C|Well-draining soil|m,w|Golden daisy flowers with dark centres.|Easy plant; deadhead for longer blooming.
Annual Phlox|Phlox drummondii|🌸|Flowering|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Clusters of colourful star-shaped flowers.|Sow in cool weather and water at the base.
Statice|Limonium sinuatum|💜|Flowering|h|l|o,b|b|10-28°C|Light, well-draining soil|w|Papery everlasting flowers popular for dried bouquets.|Water lightly and cut for drying when fully open.
Baby's Breath|Gypsophila paniculata|🤍|Flowering|h|l|o,b|b|10-25°C|Light, alkaline, well-draining soil|w|Airy clouds of tiny white flowers used in bouquets.|Water lightly and avoid soggy soil.
Agapanthus|Agapanthus africanus|💙|Flowering|h|m|o,b|b|10-30°C|Rich, well-draining soil|m|Round heads of blue flowers on tall stems.|Water regularly in summer and divide when crowded.
Clivia|Clivia miniata|🧡|Flowering|l|m|o,b|b|10-28°C|Light, well-draining soil|m,w|Shade-loving plant with orange trumpet flowers.|Keep it a little root-bound and avoid direct sun.
Lobster Claw|Heliconia rostrata|🦞|Flowering|m|h|o|e|22-35°C|Rich, moist soil|m|Dramatic hanging red and yellow bracts.|Provide humidity, shelter from wind and constant moisture.
Water Lily|Nymphaea nouchali|🪷|Flowering|h|h|o,b|b|20-35°C|Pond or tub with garden soil|s,m|Floating blue-purple flowers for ponds and tubs.|Keep water still and plant in a container of loam.
Apple|Malus domestica|🍎|Fruit,Outdoor|h|m|o|e|10-28°C|Well-draining loamy soil|w|Needs a cool climate or low-chill varieties in warm areas.|Choose a low-chill variety such as Anna and prune in winter.
Peach|Prunus persica|🍑|Fruit,Outdoor|h|m|o|e|10-30°C|Well-draining loamy soil|w|Spring-flowering tree; low-chill varieties suit warmer areas.|Choose a low-chill variety and thin fruit for size.
Plum|Prunus salicina|🍑|Fruit,Outdoor|h|m|o|e|10-30°C|Well-draining loamy soil|w|Early-flowering fruit tree; some varieties suit warm areas.|Water regularly and prune lightly in winter.
Loquat|Eriobotrya japonica|🍊|Fruit,Outdoor|h|m|o|b|10-32°C|Well-draining loamy soil|m|Evergreen tree with sweet-tart golden fruit.|Water young trees and protect from strong wind.
Longan|Dimocarpus longan|🍇|Fruit,Outdoor|h|m|o|e|20-35°C|Well-draining loamy soil|m|Tropical tree with sweet, translucent fruit.|Water regularly while young and mulch around the base.
Rambutan|Nephelium lappaceum|🍒|Fruit,Outdoor|h|h|o|e|22-35°C|Rich, moist soil|m|Hairy red fruit with sweet, juicy flesh.|Needs warmth, humidity and steady moisture.
Mangosteen|Garcinia mangostana|🍇|Fruit,Outdoor|m|h|o|e|22-35°C|Rich, moist soil|m|Slow-growing tropical tree with purple fruit.|Give humidity, shade when young and steady moisture.
Breadfruit|Artocarpus altilis|🍈|Fruit,Outdoor|h|m|o|b|22-38°C|Rich, well-draining soil|m|Large tropical tree with starchy fruit.|Give plenty of room and water regularly.
Soursop|Annona muricata|🍈|Fruit,Outdoor|h|m|o|e|22-35°C|Rich, well-draining soil|m|Tropical tree with large spiny, creamy fruit.|Protect from cold and water regularly.
Cherimoya|Annona cherimola|🍈|Fruit,Outdoor|h|m|o|e|15-30°C|Rich, well-draining soil|m|Subtropical tree with creamy, sweet fruit.|Water regularly and avoid frost and extreme heat.
Atemoya|Annona x atemoya|🍈|Fruit,Outdoor|h|m|o|e|18-35°C|Well-draining loamy soil|m|Custard apple hybrid with sweet, creamy fruit.|Hand-pollinate flowers for a better crop.
Strawberry Guava|Psidium cattleyanum|🍓|Fruit,Outdoor|h|m|o,b|b|15-35°C|Well-draining loamy soil|m|Compact guava with small red, sweet fruit.|Water regularly and prune lightly.
Pomelo|Citrus maxima|🍊|Fruit,Outdoor|h|m|o|b|18-35°C|Well-draining loamy soil|m|Largest citrus with thick rind and mild sweet flesh.|Water deeply and feed with citrus fertilizer.
Grapefruit|Citrus x paradisi|🍊|Fruit,Outdoor|h|m|o|b|18-35°C|Well-draining loamy soil|m|Tangy citrus tree that fruits well in warm areas.|Water deeply and feed regularly.
Sweet Orange|Citrus sinensis|🍊|Fruit,Outdoor|h|m|o|b|15-35°C|Well-draining loamy soil|m|Classic orange tree for large pots and gardens.|Water deeply and feed with citrus fertilizer.
Kumquat|Citrus japonica|🍊|Fruit,Outdoor|h|m|o,b|b|10-35°C|Well-draining loamy soil|m|Small citrus eaten whole, peel and all.|Water regularly and protect from heavy frost.
Kaffir Lime|Citrus hystrix|🍋|Fruit,Outdoor|h|m|o,b|b|18-35°C|Well-draining loamy soil|m|Aromatic double leaves used in Thai cooking.|Water regularly and feed with citrus fertilizer.
Lime|Citrus aurantiifolia|🍋|Fruit,Outdoor|h|m|o,b|b|18-38°C|Well-draining loamy soil|m|Thorny tree with small, tangy green fruit.|Water regularly and prune thorny branches.
Citron|Citrus medica|🍋|Fruit,Outdoor|h|m|o|b|18-35°C|Well-draining loamy soil|m|Fragrant, thick-skinned fruit used in pickles and rituals.|Water regularly and protect from frost.
Jabuticaba|Plinia cauliflora|🍇|Fruit,Outdoor|h|h|o,b|e|18-35°C|Acidic, well-draining soil|m|Grape-like fruit that grows directly on the trunk.|Keep soil moist and acidic; it grows slowly.
Acerola|Malpighia emarginata|🍒|Fruit,Outdoor|h|m|o,b|b|20-35°C|Well-draining loamy soil|m|Small shrub with red, vitamin C-rich fruit.|Water regularly and protect from cold.
Surinam Cherry|Eugenia uniflora|🍒|Fruit,Outdoor|h|m|o,b|b|18-35°C|Well-draining loamy soil|m|Bushy shrub with ribbed red, tangy fruit.|Water regularly and prune to shape.
Miracle Fruit|Synsepalum dulcificum|🍒|Fruit,Outdoor|m|m|o,b|e|20-35°C|Acidic, well-draining soil|m|Small berry that makes sour foods taste sweet.|Use acidic soil and keep it humid and warm.
Cashew|Anacardium occidentale|🥜|Fruit,Outdoor|h|l|o|b|20-38°C|Sandy, well-draining soil|m|Tropical tree with the nut hanging below a fleshy apple.|Water young trees and give plenty of sun.
Areca Nut|Areca catechu|🌴|Fruit,Outdoor|m|h|o|e|20-35°C|Rich, moist soil|m|Slender palm grown for its nuts.|Keep soil moist and shade young plants.
Cocoa|Theobroma cacao|🍫|Fruit,Outdoor|l|h|o|e|20-35°C|Rich, moist, humus soil|m|Understorey tree whose pods give chocolate beans.|Give shade, humidity and steady moisture.
Coffee|Coffea arabica|☕|Fruit,Outdoor|m|m|o,b|e|15-28°C|Rich, acidic, well-draining soil|m|Shade-loving shrub with glossy leaves and red cherries.|Give partial shade and keep soil moist.
Olive|Olea europaea|🫒|Fruit,Outdoor|h|l|o,b|b|10-38°C|Well-draining, even rocky soil|m,w|Hardy silver-leaved tree that tolerates dry weather.|Water young trees and prune to shape.
Palmyra Palm|Borassus flabellifer|🌴|Fruit,Outdoor|h|l|o|b|22-42°C|Sandy, well-draining soil|m|Tall palm tolerant of heat and drought.|Plant in a permanent spot; it grows slowly.
Egg Fruit|Pouteria campechiana|🥭|Fruit,Outdoor|h|m|o|b|20-35°C|Well-draining loamy soil|m|Tree with dry, sweet, egg-yolk-like fruit.|Water young trees regularly.
Black Sapote|Diospyros nigra|🍫|Fruit,Outdoor|h|m|o|b|20-35°C|Well-draining loamy soil|m|Tropical tree with soft, chocolate-like pulp.|Water regularly and protect from frost.
Bilimbi|Averrhoa bilimbi|🥒|Fruit,Outdoor|h|m|o,b|b|22-35°C|Rich, well-draining soil|m|Small tree with sour, cucumber-like fruit.|Water regularly and feed with compost.
Star Gooseberry|Phyllanthus acidus|🍈|Fruit,Outdoor|h|m|o|b|20-35°C|Well-draining loamy soil|m|Small tree with sour, ribbed fruit used in pickles.|Water regularly while young.
Cape Gooseberry|Physalis peruviana|🍊|Fruit,Outdoor|h|m|o,b|b|15-28°C|Light, well-draining soil|m,w|Golden berries wrapped in papery husks.|Support the plants and water regularly.
Tomato|Solanum lycopersicum|🍅|Fruit,Outdoor|h|m|o,b|b|18-30°C|Rich, well-draining loamy soil|m,w|Garden favourite that needs sun and regular feeding.|Stake the plants, water at the root and feed regularly.
Bell Pepper|Capsicum annuum var. grossum|🫑|Fruit,Outdoor|h|m|o,b|b|18-30°C|Rich, well-draining loamy soil|m,w|Mild, thick-walled peppers in green, red or yellow.|Water evenly and support heavy branches.
Brinjal|Solanum melongena|🍆|Fruit,Outdoor|h|m|o,b|b|20-35°C|Rich, well-draining loamy soil|s,m,w|Eggplant that fruits for months in warm weather.|Water regularly, feed often and pick fruit young.
Okra|Abelmoschus esculentus|🌿|Fruit,Outdoor|h|m|o,b|b|22-38°C|Well-draining loamy soil|s,m|Heat-loving vegetable (bhindi) that grows fast.|Harvest young pods every day or two.
Cucumber|Cucumis sativus|🥒|Fruit,Outdoor|h|h|o,b|b|18-35°C|Rich, well-draining loamy soil|s,m|Fast-growing climber with crisp fruit.|Provide a trellis and water regularly.
Pumpkin|Cucurbita moschata|🎃|Fruit,Outdoor|h|m|o|b|20-35°C|Rich, well-draining soil|s,m|Sprawling vine that bears large, long-keeping fruit.|Give plenty of space and water at the base.
Bottle Gourd|Lagenaria siceraria|🥒|Fruit,Outdoor|h|m|o,b|b|20-38°C|Rich, well-draining soil|s,m|Vigorous climber with long pale-green fruit (lauki).|Provide a strong trellis and water regularly.
Bitter Gourd|Momordica charantia|🥒|Fruit,Outdoor|h|m|o,b|b|20-35°C|Rich, well-draining soil|s,m|Climbing vine with warty green fruit (karela).|Provide a trellis and pick fruit while still green.
Ridge Gourd|Luffa acutangula|🥒|Fruit,Outdoor|h|m|o,b|b|22-38°C|Rich, well-draining soil|s,m|Vigorous climber with ridged green fruit (turai).|Provide a trellis and pick fruit young.
Snake Gourd|Trichosanthes cucumerina|🥒|Fruit,Outdoor|h|m|o,b|b|22-38°C|Rich, well-draining soil|s,m|Climber with long, slender fruit.|Provide a trellis and water regularly.
Ash Gourd|Benincasa hispida|🥒|Fruit,Outdoor|h|m|o|b|22-38°C|Rich, well-draining soil|s,m|Large vine with waxy, long-keeping fruit (petha).|Give space and water at the base.
Ivy Gourd|Coccinia grandis|🥒|Fruit,Outdoor|h|m|o,b|b|20-38°C|Well-draining soil|s,m|Hardy perennial climber with small fruit (tindora).|Provide a trellis; it spreads quickly.
Chayote|Sechium edule|🥒|Fruit,Outdoor|h|m|o|b|15-30°C|Rich, well-draining soil|m|Vigorous climber with pear-shaped green fruit.|Plant the whole sprouted fruit and provide a trellis.
Pointed Gourd|Trichosanthes dioica|🥒|Fruit,Outdoor|h|m|o|b|22-38°C|Well-draining loamy soil|s,m|Creeping vine with small striped green fruit (parwal).|Grow from cuttings and keep soil moist.
Sweet Corn|Zea mays|🌽|Fruit,Outdoor|h|m|o|b|18-35°C|Rich, well-draining soil|s,m|Fast-growing grain crop eaten fresh.|Plant in blocks for good pollination and water regularly.
Water Apple|Syzygium samarangense|🍎|Fruit,Outdoor|h|h|o|b|22-35°C|Rich, moist soil|m|Bell-shaped, crisp, juicy fruit on a tropical tree.|Keep soil moist and water young trees regularly.
Vana Tulsi|Ocimum gratissimum|🌿|Medicinal,Herb|h|m|o,b|b|20-35°C|Well-draining soil|s,m|Tall, clove-scented basil traditionally used in home remedies.|Water regularly and prune to keep it bushy.
Lemon Verbena|Aloysia citrodora|🍋|Medicinal,Herb|h|m|o,b|b|10-30°C|Well-draining soil|s,m|Lemon-scented leaves used for herbal tea.|Water regularly and protect from frost.
Black Turmeric|Curcuma caesia|🌿|Medicinal|m|m|o,b|b|20-35°C|Rich, well-draining soil|m|Rare turmeric with a bluish-black rhizome.|Plant rhizomes in the monsoon and avoid waterlogging.
Mango Ginger|Curcuma amada|🌿|Medicinal|m|m|o,b|b|20-35°C|Rich, well-draining soil|m|Rhizome that smells of raw mango, used in pickles.|Plant rhizomes in the monsoon and keep soil moist.
Galangal|Alpinia galanga|🌿|Medicinal,Herb|m|m|o,b|b|20-35°C|Rich, well-draining soil|m|Peppery rhizome used in Southeast Asian cooking.|Keep soil moist and give partial shade.
Fingerroot|Boesenbergia rotunda|🌿|Medicinal,Herb|m|m|o,b|b|20-35°C|Rich, well-draining soil|m|Slender rhizomes used in Thai cooking.|Keep soil moist and shade from harsh sun.
Citronella|Cymbopogon nardus|🌾|Medicinal,Herb|h|m|o,b|b|20-35°C|Well-draining soil|s,m|Tall aromatic grass traditionally used as a mosquito-repelling plant.|Water regularly and divide clumps.
Vetiver|Chrysopogon zizanioides|🌾|Medicinal,Outdoor|h|l|o|b|20-38°C|Well-draining soil|m|Deep-rooted fragrant grass used for cooling and soil protection.|Plant slips in the monsoon; it needs little care.
Sandalwood|Santalum album|🌳|Medicinal,Outdoor|h|l|o|e|18-35°C|Well-draining soil|m|Fragrant tree that needs a host plant for its roots.|Grow with a host such as pigeon pea and water lightly.
Ashoka Tree|Saraca asoca|🌳|Medicinal,Outdoor|m|m|o|b|20-35°C|Rich, moist soil|m|Sacred evergreen tree with fragrant orange flowers.|Keep soil moist and give light shade when young.
Karanj|Pongamia pinnata|🌳|Medicinal,Outdoor|h|l|o|b|20-40°C|Well-draining soil|m|Hardy shade tree traditionally used for oil and medicine.|Water young trees; hardy once established.
Mahua|Madhuca longifolia|🌳|Medicinal,Outdoor|h|l|o|b|20-40°C|Well-draining soil|m|Large tree important in rural Indian culture.|Plant in a permanent spot and water young trees.
Kutaj|Holarrhena pubescens|🌿|Medicinal,Outdoor|h|l|o|b|20-38°C|Well-draining soil|m|Small tree with white flowers used in traditional medicine.|Water young plants and avoid waterlogging.
Gokshura|Tribulus terrestris|🌿|Medicinal|h|l|o,b|b|20-38°C|Sandy, well-draining soil|s,m|Spreading herb with spiny fruit, traditionally used in remedies.|Water lightly; the spiny fruits can hurt bare feet.
Kapikacchu|Mucuna pruriens|🌿|Medicinal|h|m|o|b|20-35°C|Rich, well-draining soil|m|Climbing legume; the pods have irritating hairs.|Wear gloves when handling and provide a support.
Kantakari|Solanum virginianum|🌿|Medicinal|h|l|o,b|b|20-38°C|Sandy, well-draining soil|s,m|Prickly low herb traditionally used in remedies.|Wear gloves and water lightly.
Bala|Sida cordifolia|🌿|Medicinal|h|l|o,b|b|20-38°C|Well-draining soil|m|Small shrub traditionally used in Ayurveda.|Water lightly and prune to shape.
Atibala|Abutilon indicum|🌼|Medicinal|h|l|o,b|b|20-38°C|Well-draining soil|m|Hardy shrub with small yellow flowers, traditionally used in remedies.|Water lightly and cut back after flowering.
Guggul|Commiphora wightii|🌳|Medicinal,Outdoor|h|l|o|e|20-40°C|Sandy, well-draining soil|m|Thorny desert shrub that yields a fragrant resin.|Water sparingly and give full sun.
Shalparni|Desmodium gangeticum|🌿|Medicinal|m|m|o|b|20-35°C|Well-draining soil|m|Small shrub traditionally used in Ayurvedic preparations.|Water regularly and prune lightly.
Lodhra|Symplocos racemosa|🌳|Medicinal,Outdoor|m|m|o|b|15-35°C|Rich, well-draining soil|m|Small tree traditionally used for its bark.|Water young plants regularly.
Nirgundi|Vitex negundo|🌿|Medicinal,Outdoor|h|l|o|b|18-38°C|Well-draining soil|m|Aromatic shrub traditionally used for pain relief.|Water young plants and prune to shape.
Agnimantha|Premna serratifolia|🌳|Medicinal,Outdoor|h|m|o|b|20-38°C|Well-draining soil|m|Small tree used in the Dashamoola group of herbs.|Water regularly while young.
Cinnamon|Cinnamomum verum|🌿|Medicinal,Herb|m|m|o|e|20-35°C|Rich, well-draining soil|m|Tree grown for its aromatic inner bark.|Keep soil moist and prune to keep it shrubby.
Indian Bay Leaf|Cinnamomum tamala|🍃|Medicinal,Herb|m|m|o|b|15-35°C|Rich, well-draining soil|m|Tree whose leaves (tej patta) flavour Indian cooking.|Water regularly while young.
Clove|Syzygium aromaticum|🌿|Medicinal,Herb|m|h|o|e|20-35°C|Rich, moist soil|m|Tropical tree grown for its dried flower buds.|Give humidity, shade when young and steady moisture.
Nutmeg|Myristica fragrans|🌰|Medicinal,Herb|m|h|o|e|20-35°C|Rich, moist soil|m|Tropical tree that gives both nutmeg and mace.|Give shade when young and keep soil moist.
Vanilla|Vanilla planifolia|🌿|Medicinal,Herb|m|h|o|e|20-32°C|Airy, humus-rich mix|m|Climbing orchid grown for its fragrant pods.|Provide a support, humidity and partial shade.
Saffron|Crocus sativus|🌸|Medicinal,Herb|h|l|o,b|e|5-20°C|Light, well-draining soil|w|Needs a cool climate; stigmas are harvested as spice.|Plant corms in autumn and avoid waterlogging.
Licorice|Glycyrrhiza glabra|🌿|Medicinal|h|m|o|b|10-35°C|Deep, sandy loam|m,w|Deep-rooted perennial grown for its sweet roots.|Plant in deep soil and water regularly.
Valerian|Valeriana officinalis|🌸|Medicinal|m|m|o|b|10-25°C|Rich, moist soil|w|Tall plant with pink flowers; the roots are used traditionally.|Keep soil moist and give partial shade.
St John's Wort|Hypericum perforatum|🌼|Medicinal|h|l|o,b|b|10-30°C|Well-draining soil|w|Yellow-flowered perennial used in herbal medicine.|Water lightly; it may interact with medicines.
Feverfew|Tanacetum parthenium|🌼|Medicinal|h|m|o,b|b|10-25°C|Well-draining soil|w|Daisy-like flowers on a bushy herb.|Deadhead often and water regularly.
Yarrow|Achillea millefolium|🌼|Medicinal|h|l|o|b|10-30°C|Well-draining soil|w|Hardy perennial with flat clusters of white flowers.|Water lightly and divide every few years.
Comfrey|Symphytum officinale|💜|Medicinal|m|m|o|b|10-28°C|Rich, moist soil|m,w|Deep-rooted plant; avoid eating it.|Use the leaves as compost and avoid ingestion.
Marshmallow|Althaea officinalis|🌸|Medicinal|h|m|o|b|10-30°C|Moist, loamy soil|w|Tall plant with soft grey leaves and pale pink flowers.|Keep soil moist and cut back after flowering.
Elderberry|Sambucus nigra|🫐|Medicinal,Fruit|h|m|o|e|5-28°C|Rich, moist soil|w|Large shrub with flowers and berries; raw parts are toxic.|Cook the berries and avoid eating raw parts.
Roselle|Hibiscus sabdariffa|🌺|Medicinal,Herb|h|m|o,b|b|20-38°C|Well-draining soil|s,m|Red calyces and tangy leaves (gongura/ambadi) used in food and drinks.|Water regularly and harvest the calyces when plump.
Passionflower|Passiflora incarnata|🌸|Medicinal,Flowering|h|m|o,b|b|15-35°C|Well-draining soil|s,m|Intricate flowers on a vigorous vine.|Provide a trellis and water regularly.
Wormwood|Artemisia absinthium|🌿|Medicinal|h|l|o|b|10-30°C|Well-draining soil|w|Silver-grey bitter herb; toxic in large amounts.|Water lightly and use only in small amounts.
Mugwort|Artemisia vulgaris|🌿|Medicinal|h|m|o|b|10-30°C|Well-draining soil|w|Hardy aromatic herb that spreads easily.|Contain its roots and water lightly.
Milk Thistle|Silybum marianum|🌸|Medicinal|h|l|o|b|10-30°C|Well-draining soil|w|Spiny plant with purple flowers and marbled leaves.|Wear gloves and water lightly.
Dandelion|Taraxacum officinale|🌼|Medicinal,Herb|h|m|o,b|b|5-28°C|Light, well-draining soil|w|Edible leaves and roots with cheerful yellow flowers.|Harvest leaves young before flowering.
Stinging Nettle|Urtica dioica|🌿|Medicinal,Herb|m|m|o|b|5-25°C|Rich, moist soil|w|Leaves sting until cooked or dried.|Wear gloves when handling.
Common Plantain|Plantago major|🌿|Medicinal|h|m|o|b|5-30°C|Average, well-draining soil|m,w|Hardy low-growing rosette with edible leaves.|Easy to grow; harvest leaves as needed.
Chicory|Cichorium intybus|💙|Medicinal,Herb|h|m|o|b|10-30°C|Well-draining soil|w|Blue flowers and a taproot used as a coffee substitute.|Sow in cool weather and water regularly.
Soapnut|Sapindus mukorossi|🌳|Medicinal,Outdoor|h|m|o|b|15-38°C|Well-draining soil|m|Tree whose fruits (reetha) are used as natural soap.|Water young trees regularly.
Shikakai|Senegalia rugata|🌿|Medicinal,Outdoor|h|l|o|b|20-38°C|Well-draining soil|m|Thorny climbing shrub whose pods are used for hair care.|Wear gloves and give a support.
Sacred Fig|Ficus religiosa|🌳|Medicinal,Outdoor|h|m|o|b|18-38°C|Well-draining soil|m|Large sacred tree (peepal); roots are strong and spreading.|Plant far from buildings and pipes.
Banyan|Ficus benghalensis|🌳|Medicinal,Outdoor|h|m|o|b|18-40°C|Well-draining soil|m|Huge tree with aerial roots (vad); needs lots of space.|Plant far from buildings and give it plenty of room.
Hyssop|Hyssopus officinalis|💜|Herb|h|l|o,b|b|10-28°C|Light, well-draining soil|w|Aromatic herb with blue-purple flowers.|Water lightly and prune after flowering.
Chervil|Anthriscus cerefolium|🌿|Herb|m|m|o,b|b|10-22°C|Moist, rich soil|w|Delicate anise-flavoured leaves for French dishes.|Sow in cool weather and shade from hot sun.
Lovage|Levisticum officinale|🌿|Herb|h|m|o|b|10-25°C|Rich, moist soil|w|Tall celery-flavoured herb.|Keep soil moist and cut back to encourage growth.
Winter Savory|Satureja montana|🌿|Herb|h|l|o,b|b|10-28°C|Light, well-draining soil|w|Hardy peppery herb for beans and meats.|Water lightly and trim after flowering.
Greek Oregano|Origanum vulgare subsp. hirtum|🌿|Herb|h|l|o,b|b|10-30°C|Light, well-draining soil|w,m|Strongly flavoured oregano for cooking.|Water lightly and harvest regularly.
Culantro|Eryngium foetidum|🌿|Herb|m|m|o,b|b|18-35°C|Rich, moist soil|m|Long serrated leaves with a strong coriander flavour.|Keep soil moist and shade from hot sun.
Lemon Basil|Ocimum x citriodorum|🌿|Herb|h|m|i,o,b|b|18-32°C|Rich, well-draining soil|s,m|Basil with a bright citrus scent.|Pinch flowers and water when the top soil dries.
Curry Plant|Helichrysum italicum|🌿|Herb|h|l|o,b|b|10-30°C|Sandy, well-draining soil|s,w|Silvery leaves with a curry-like aroma; used for scent.|Water lightly and prune to shape.
Shiso|Perilla frutescens|🌿|Herb|m|m|o,b|b|15-32°C|Rich, well-draining soil|s,m|Aromatic purple or green leaves used in Asian cooking.|Pinch tips and keep soil moist.
Epazote|Dysphania ambrosioides|🌿|Herb|h|l|o|b|15-32°C|Light, well-draining soil|s,m|Pungent herb used with beans in Mexican cooking.|Use leaves sparingly and water lightly.
Pennyroyal|Mentha pulegium|🌿|Herb|m|h|o,b|b|10-28°C|Moist, rich soil|m,w|Creeping mint with a strong aroma; unsafe in pregnancy.|Keep soil moist and do not eat large amounts.
Apple Mint|Mentha suaveolens|🌿|Herb|m|h|o,b|b|10-28°C|Moist, rich soil|m,w|Fuzzy leaves with a fruity minty flavour.|Keep soil moist and grow in its own pot.
Water Mint|Mentha aquatica|🌿|Herb|m|h|o,b|b|10-28°C|Moist to wet soil|m,w|Mint that grows well at pond edges and in wet soil.|Keep roots wet and grow in a contained pot.
Garden Cress|Lepidium sativum|🌱|Herb|m|m|i,o,b|b|10-25°C|Light, well-draining soil|w|Very fast peppery greens (halim) ready in about two weeks.|Sow thickly and keep soil moist.
Watercress|Nasturtium officinale|🌱|Herb|m|h|o,b|b|10-22°C|Wet, rich soil|w|Peppery leaves that grow in running or constantly wet soil.|Keep roots wet and harvest from shallow water.
Spinach|Spinacia oleracea|🥬|Herb|m|m|o,b|b|10-25°C|Rich, well-draining soil|w|Quick leafy vegetable that likes cool weather.|Sow in winter and harvest outer leaves.
Malabar Spinach|Basella alba|🥬|Herb|h|m|o,b|b|20-38°C|Rich, well-draining soil|s,m|Heat-loving climbing spinach (poi).|Provide a trellis and harvest tender shoots.
Amaranth|Amaranthus tricolor|🥬|Herb|h|m|o,b|b|20-38°C|Well-draining soil|s,m|Quick-growing leafy vegetable (chaulai) loved in hot weather.|Water regularly and harvest young leaves.
Lettuce|Lactuca sativa|🥬|Herb|m|m|o,b|b|10-24°C|Rich, moist soil|w|Crisp salad leaves that prefer cool weather.|Sow in winter and keep soil moist.
Kale|Brassica oleracea var. sabellica|🥬|Herb|h|m|o,b|b|10-25°C|Rich, well-draining soil|w|Hardy, nutritious leafy brassica.|Harvest outer leaves and water regularly.
Swiss Chard|Beta vulgaris subsp. vulgaris|🥬|Herb|m|m|o,b|b|10-28°C|Rich, well-draining soil|w,m|Colourful stems with broad leaves; harvest repeatedly.|Pick outer leaves and keep soil moist.
Radish|Raphanus sativus|🥕|Herb|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Fast root vegetable ready in about a month.|Sow in cool weather and water evenly.
Carrot|Daucus carota|🥕|Herb|h|m|o,b|b|10-25°C|Loose, deep, stone-free soil|w|Sweet roots that need loose soil to grow straight.|Sow directly and thin seedlings.
Bok Choy|Brassica rapa subsp. chinensis|🥬|Herb|m|m|o,b|b|10-25°C|Rich, well-draining soil|w|Mild, crisp Chinese cabbage ready in 45 days.|Sow in cool weather and keep soil moist.
Cabbage|Brassica oleracea var. capitata|🥬|Herb|h|m|o,b|b|10-25°C|Rich, well-draining soil|w|Cool-season vegetable that forms firm heads.|Water evenly and watch for caterpillars.
Cauliflower|Brassica oleracea var. botrytis|🥦|Herb|h|m|o,b|e|10-22°C|Rich, well-draining soil|w|Cool-season crop that forms white curds.|Keep soil moist and shade the curd with leaves.
Broccoli|Brassica oleracea var. italica|🥦|Herb|h|m|o,b|b|10-24°C|Rich, well-draining soil|w|Cool-season crop with green flower heads.|Water evenly and harvest before flowers open.
Onion|Allium cepa|🧅|Herb|h|m|o,b|b|10-28°C|Loose, well-draining soil|w|Bulb crop grown from seed or sets in winter.|Stop watering when the tops fall over.
Leek|Allium porrum|🌱|Herb|h|m|o,b|b|10-25°C|Rich, well-draining soil|w|Mild onion relative with thick white stems.|Hill soil around stems and water regularly.
Shallot|Allium cepa var. aggregatum|🧅|Herb|h|m|o,b|b|10-30°C|Well-draining loamy soil|w,m|Clustering small onions with a sweet flavour.|Plant bulbs shallowly and water lightly.
Garden Pea|Pisum sativum|🌱|Herb|h|m|o,b|b|10-22°C|Rich, well-draining soil|w|Sweet climbing pods for cool seasons.|Provide a trellis and pick often.
French Beans|Phaseolus vulgaris|🫘|Herb|h|m|o,b|b|15-30°C|Rich, well-draining soil|m,w|Easy bush or climbing beans that crop quickly.|Water regularly and pick young pods.
Cumin|Cuminum cyminum|🌿|Herb|h|l|o,b|e|15-30°C|Light, well-draining soil|w|Cool-season spice crop grown for its seeds.|Sow directly and water lightly.
Caraway|Carum carvi|🌿|Herb|h|m|o|b|10-25°C|Rich, well-draining soil|w|Biennial herb grown for aromatic seeds.|Sow directly in cool weather.
Black Mustard|Brassica nigra|🌼|Herb|h|m|o,b|b|10-25°C|Well-draining soil|w|Quick winter crop with yellow flowers and spicy seeds.|Sow thickly and thin as needed.
Sesame|Sesamum indicum|🌼|Herb|h|l|o|b|22-38°C|Well-draining, sandy loam|s,m|Heat-loving oilseed with pale bell-shaped flowers.|Water lightly and do not overwater.
Sweet Cicely|Myrrhis odorata|🌿|Herb|m|m|o|b|5-22°C|Moist, rich soil|w|Ferny, anise-scented herb for cool climates.|Keep soil moist and shade from hot sun.
Salad Burnet|Poterium sanguisorba|🌿|Herb|h|l|o,b|b|10-28°C|Light, well-draining soil|w|Cucumber-flavoured leaves for salads.|Water lightly and cut flowers off.
Purslane|Portulaca oleracea|🌿|Herb|h|l|o,b|b|18-38°C|Light, well-draining soil|s,m|Succulent edible leaves that thrive in heat.|Easy to grow; harvest tender shoots.
Bathua|Chenopodium album|🥬|Herb|h|m|o,b|b|10-28°C|Rich, well-draining soil|w|Winter leafy green used in Indian dishes.|Sow in cool weather and harvest young leaves.
Agathi|Sesbania grandiflora|🌿|Herb|h|m|o|b|20-38°C|Well-draining soil|s,m|Fast-growing tree with edible flowers and leaves.|Water young plants and prune to shape.
Colocasia|Colocasia esculenta|🍃|Herb|m|h|o,b|b|20-35°C|Rich, moist soil|s,m|Leaves and corms (arbi) are cooked as food; raw leaves irritate.|Keep soil moist and cook thoroughly before eating.
Water Spinach|Ipomoea aquatica|🥬|Herb|h|h|o,b|b|20-38°C|Wet, rich soil|s,m|Fast-growing hollow-stemmed greens (kangkong).|Keep soil wet and harvest shoots often.
Sweet Potato|Ipomoea batatas|🍠|Herb|h|m|o,b|b|20-35°C|Loose, well-draining soil|s,m|Trailing vine with edible tubers and leaves.|Plant cuttings and keep soil evenly moist.
Wheatgrass|Triticum aestivum|🌾|Herb|h|m|i,b|b|15-28°C|Light potting mix|s,m,w|Quick grass grown in trays for juice.|Sow thickly and harvest in about 8 days.
Lemon Myrtle|Backhousia citriodora|🍋|Herb|h|m|o,b|e|15-32°C|Rich, well-draining soil|m|Shrub with strong lemony-scented leaves for teas.|Water regularly and protect from frost.
Bee Balm|Monarda didyma|🌺|Herb|h|m|o,b|b|10-28°C|Rich, moist soil|w,m|Scarlet flowers loved by bees and used in tea.|Keep soil moist and divide every few years.
Roman Chamomile|Chamaemelum nobile|🌼|Herb|h|m|o,b|b|10-25°C|Light, well-draining soil|w|Low-growing carpet with apple-scented daisy flowers.|Water lightly and pick flowers for tea.
Anise Hyssop|Agastache foeniculum|💜|Herb|h|m|o,b|b|10-28°C|Light, well-draining soil|w,m|Licorice-scented leaves and purple flower spikes.|Deadhead for more flowers and water lightly.
Mexican Oregano|Lippia graveolens|🌿|Herb|h|l|o,b|b|15-35°C|Sandy, well-draining soil|s,m|Strongly flavoured shrub used in Mexican cooking.|Water lightly and prune to shape.
Silver Oak|Grevillea robusta|🌳|Outdoor|h|m|o|b|15-35°C|Well-draining soil|m|Fast-growing, feathery-leaved tree often used for avenues.|Water young trees and give plenty of space.
Rain Tree|Samanea saman|🌳|Outdoor|h|m|o|b|20-38°C|Well-draining soil|m|Huge spreading shade tree with a wide canopy.|Give lots of space and avoid planting near buildings.
Copper Pod|Peltophorum pterocarpum|🌳|Outdoor|h|m|o|b|20-38°C|Well-draining soil|m|Spreading tree with yellow flowers and rusty pods.|Water young trees and prune lightly.
Golden Shower|Cassia fistula|🌼|Outdoor,Flowering|h|m|o|b|20-40°C|Well-draining soil|m|Showy tree with long chains of yellow flowers in summer.|Water young trees and give plenty of sun.
Pink Cassia|Cassia javanica|🌸|Outdoor,Flowering|h|m|o|b|20-38°C|Well-draining soil|m|Tree with large clusters of pink and white flowers.|Water young trees and prune to shape.
Flame of the Forest|Butea monosperma|🔥|Outdoor,Flowering|h|l|o|b|20-40°C|Well-draining soil|m|Tree covered in orange-red flowers (palash) in spring.|Water young trees; hardy once established.
Coral Tree|Erythrina variegata|🌺|Outdoor,Flowering|h|m|o|b|20-38°C|Well-draining soil|m|Thorny tree with striking red flowers on bare branches.|Give space and prune to shape.
African Tulip Tree|Spathodea campanulata|🌺|Outdoor,Flowering|h|m|o|b|20-38°C|Well-draining soil|m|Large tree with showy orange-red tulip-like flowers.|Give lots of space; branches can be brittle.
Kadamba|Neolamarckia cadamba|🌳|Outdoor|h|m|o|b|20-38°C|Moist, well-draining soil|m|Fast-growing tree with round, fragrant flower balls.|Water young trees regularly and give space.
Indian Cork Tree|Millingtonia hortensis|🌳|Outdoor,Flowering|h|m|o|b|20-38°C|Well-draining soil|m|Tall tree with fragrant white night-blooming flowers.|Water young trees and plant with plenty of space.
Cannonball Tree|Couroupita guianensis|🌳|Outdoor,Flowering|h|m|o|e|22-38°C|Rich, moist soil|m|Sacred tree with large cannonball fruits and strange flowers.|Water regularly; fruit may fall heavily.
Indian Almond|Terminalia catappa|🌳|Outdoor|h|m|o|b|20-38°C|Well-draining soil|m|Tiered, spreading shade tree with large leaves.|Water young trees and give space.
Saptaparni|Alstonia scholaris|🌳|Outdoor|h|m|o|b|20-38°C|Well-draining soil|m|Tall tree with whorled leaves and scented flowers.|Water young trees regularly.
Champa|Magnolia champaca|🌼|Outdoor,Flowering|h|m|o|b|18-35°C|Rich, well-draining soil|m|Tall tree with intensely fragrant orange-yellow flowers.|Water regularly and mulch around the base.
Bakul|Mimusops elengi|🌼|Outdoor,Flowering|h|m|o|b|20-38°C|Well-draining soil|m|Evergreen tree with tiny, long-lasting fragrant flowers.|Water young trees and give space.
Kachnar|Bauhinia variegata|🌸|Outdoor,Flowering|h|m|o|b|15-35°C|Well-draining soil|m|Medium tree with orchid-like pink flowers in winter.|Water young trees and prune lightly.
Chinese Banyan|Ficus microcarpa|🌳|Outdoor|h|m|o|b|15-38°C|Well-draining soil|m|Dense, glossy-leaved tree often shaped as bonsai.|Plant away from pipes; roots spread widely.
Casuarina|Casuarina equisetifolia|🌲|Outdoor|h|l|o|b|20-40°C|Sandy, well-draining soil|m|Fast-growing, wind-tolerant tree with needle-like branchlets.|Plant as a windbreak and water young trees.
Teak|Tectona grandis|🌳|Outdoor|h|m|o|b|20-38°C|Deep, well-draining soil|m|Valuable timber tree that grows tall and straight.|Water young trees and give plenty of space.
Indian Rosewood|Dalbergia sissoo|🌳|Outdoor|h|m|o|b|15-40°C|Well-draining soil|m|Strong timber tree that tolerates dry spells.|Water young trees and give space.
Eucalyptus|Eucalyptus globulus|🌳|Outdoor|h|m|o|b|10-35°C|Well-draining soil|m|Very fast-growing aromatic tree.|Plant away from buildings; roots and water use are high.
Chir Pine|Pinus roxburghii|🌲|Outdoor|h|m|o|b|10-30°C|Well-draining soil|m|Tall evergreen with long needles for hill areas.|Water young trees and plant in a permanent spot.
Italian Cypress|Cupressus sempervirens|🌲|Outdoor|h|m|o|b|10-35°C|Well-draining soil|m|Tall, narrow evergreen that forms natural columns.|Water young trees and avoid waterlogging.
Araucaria|Araucaria heterophylla|🎄|Outdoor|h|m|o,b|b|10-30°C|Well-draining soil|m|Symmetrical, Christmas-tree-like evergreen.|Water young trees regularly and shelter from strong wind.
Chinese Juniper|Juniperus chinensis|🌲|Outdoor|h|l|o,b|b|10-35°C|Well-draining soil|m,w|Hardy evergreen shrub used for hedges and bonsai.|Water lightly and trim to shape.
Royal Palm|Roystonea regia|🌴|Outdoor|h|m|o|b|20-38°C|Rich, well-draining soil|m|Tall, majestic palm with a smooth grey trunk.|Give plenty of space and water regularly.
Queen Palm|Syagrus romanzoffiana|🌴|Outdoor|h|m|o|b|15-35°C|Rich, well-draining soil|m|Feathery palm that grows fast in warm areas.|Water regularly and feed with palm fertilizer.
Chinese Fan Palm|Livistona chinensis|🌴|Outdoor|m|m|o,b|b|10-35°C|Well-draining soil|m|Fan-shaped leaves on a slow-growing palm.|Water regularly and give partial sun.
Washingtonia Palm|Washingtonia robusta|🌴|Outdoor|h|m|o|b|10-40°C|Well-draining soil|m|Tall fan palm that tolerates heat and drought.|Plant in full sun and give space.
Pygmy Date Palm|Phoenix roebelenii|🌴|Outdoor|m|m|o,b|b|15-35°C|Well-draining soil|m|Compact, graceful palm with sharp thorns at the base.|Wear gloves and water regularly.
Triangle Palm|Dypsis decaryi|🌴|Outdoor|h|m|o|b|15-38°C|Well-draining soil|m|Palm with three-sided trunk and arching blue-green fronds.|Water regularly and give full sun.
Traveller's Palm|Ravenala madagascariensis|🌴|Outdoor|h|h|o|b|20-38°C|Rich, moist soil|m|Giant fan-shaped plant that stores water in its stems.|Give lots of space and water regularly.
Spindle Palm|Hyophorbe verschaffeltii|🌴|Outdoor|h|m|o,b|b|20-35°C|Well-draining soil|m|Palm with a swollen, spindle-shaped trunk.|Give sun, water moderately and protect from cold.
Boxwood|Buxus sempervirens|🌿|Outdoor|m|m|o,b|b|5-30°C|Well-draining soil|m,w|Dense evergreen shrub often clipped into shapes.|Trim regularly; all parts are toxic if eaten.
Privet|Ligustrum ovalifolium|🌿|Outdoor|h|m|o|b|10-35°C|Well-draining soil|m|Fast-growing evergreen hedge plant.|Trim regularly; berries are toxic.
Poinsettia|Euphorbia pulcherrima|🎄|Outdoor,Flowering|h|m|o,b|e|15-28°C|Well-draining soil|w|Red bracts in winter; sap is irritating.|Give 6 hours of sun and avoid waterlogging.
Jatropha|Jatropha integerrima|🌺|Outdoor,Flowering|h|l|o,b|b|20-38°C|Well-draining soil|s,m|Compact shrub with bright red flowers all year.|Water lightly; the seeds are toxic.
Copperleaf|Acalypha wilkesiana|🍂|Outdoor|h|m|o,b|b|20-38°C|Well-draining soil|s,m|Colourful bronze, red and pink foliage shrub.|Water regularly and prune to shape.
Screw Pine|Pandanus tectorius|🌴|Outdoor|h|m|o|b|20-38°C|Sandy, well-draining soil|m|Spiral leaves on stilt roots; tolerates salty air.|Wear gloves because leaf edges are spiny.
Mauritius Hemp|Furcraea foetida|🌿|Outdoor|h|l|o|b|15-38°C|Sandy, well-draining soil|s,m|Large rosette of sword-like leaves.|Water lightly and give space.
Fountain Grass|Cenchrus setaceus|🌾|Outdoor|h|m|o,b|b|10-38°C|Well-draining soil|m|Arching grass with soft bottlebrush plumes.|Trim old foliage in winter and water regularly.
Zebra Grass|Miscanthus sinensis|🌾|Outdoor|h|m|o|b|10-35°C|Well-draining soil|m|Tall ornamental grass with striped leaves.|Water regularly and cut back each year.
Golden Bamboo|Bambusa vulgaris|🎍|Outdoor|h|m|o|b|15-38°C|Rich, well-draining soil|m|Clumping bamboo with golden stems.|Water regularly and mulch.
Buddha Belly Bamboo|Bambusa ventricosa|🎍|Outdoor|h|m|o,b|b|15-35°C|Rich, well-draining soil|m|Dwarf bamboo with swollen, belly-like stems.|Water regularly and keep stems stressed for the belly shape.
Boston Ivy|Parthenocissus tricuspidata|🍁|Outdoor|m|m|o|b|5-35°C|Well-draining soil|m,w|Self-clinging vine that turns red in autumn.|Water regularly and prune to control spread.
Creeping Fig|Ficus pumila|🌿|Outdoor|m|m|o,b|b|10-35°C|Well-draining soil|m|Small-leaved vine that clings to walls.|Water regularly and prune hard to control spread.
Star Jasmine|Trachelospermum jasminoides|🌼|Outdoor,Flowering|h|m|o,b|b|10-35°C|Well-draining soil|s,m|Fragrant white star flowers on a glossy evergreen vine.|Provide a trellis and prune after flowering.
Wisteria|Wisteria sinensis|💜|Outdoor,Flowering|h|m|o|e|5-30°C|Well-draining soil|w|Heavy climber with hanging purple flower clusters.|Provide a strong support and prune twice a year.
Trumpet Creeper|Campsis radicans|🧡|Outdoor,Flowering|h|m|o|b|10-38°C|Well-draining soil|m|Vigorous vine with orange trumpet flowers.|Give a strong support and prune to control spread.
Bermuda Grass|Cynodon dactylon|🌱|Outdoor|h|m|o|b|15-40°C|Well-draining soil|s,m|Tough lawn grass (doob) for sunny gardens.|Mow regularly and water in dry weather.
"""
