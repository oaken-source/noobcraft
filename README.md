# noobcraft

## Rule Set "Blobs"

######Units
* Size (both visual, as well as 'physical' (collision)) depends on the amount of resources a unit currently possesses
* Movement costs are a percentage of the resources possessed (moving is more expensive for bigger units)
* Resource production are a percentage of the resources possessed (bigger units produce resources faster)
* Units can only divide, when they reached a fixed size
* Units can only divide into two new units, each being half the size of the former unit
* In a fight both fighting units loose the same amount of resources.
* If a unit runs out of resources, it dies.
* Costs (for Upgrades) should be auto-balancing
  * e.g. by following economic rules
    * the more an upgrade is purchased by anyone/the player, the more expensive it will get
* Resources can be transfered for free to adjacent units

######Unit Skills
* Move
* Fight
* Transfer resources

##### Upgrades
anything probably: move faster, do more dmg, produce more resources, allow dividing with smaller resources, ...
tba

## Rule Set "Items"

Idea: 
Upgrades as items that can be traded and has a weight (additional movement costs).
Buildings could be realized similarly (super heavy, more powerful, can be used if unit resides there)

######Players 
The game is played by a number of _players_. 
_Players_ control _units_ that interact with the _world_.

######World
As a _player_ you have access to the _world_ object. 
It will provide you with information about the _map_ and all _units_ visible to you.

######Map
The _map_ is the area a unit can move around in. 
It is populated by all the _units_ in the game.
If there are resources in the game, they are realized as _items_ positioned on the ground.

######Units
A _unit_ belongs to a _player_. 
It has a location on the _map_.
In each round, a _unit_ may use each and all the _items_ it is in the range of.

######Items
An _item_ has a location on the _map_.
Every _unit_ within its _radius_ can use it, if it is _powered_ up.
Each round, the _power_ of all _items_ is _refilled_ by its _refill value_ up to its _max value_.
Using an item will deplete its _power_ according to its _power cost_ formula.

Basic _items_ a player (and thus its first unit) starts the game with:

| Type                      | Power°                | Radius     | Weight | Power Cost and impact                                | Target |
|---------------------------|-----------------------|:----------:|:------:|------------------------------------------------------|--------|
| Horizontal Vision         |   5 /   7 /   5 /  10 | 0          | 5      | horizontal vision range                              | World  |
| Vertical Vision           |   5 /   7 /   5 /  10 | 0          | 5      | vertical vision range                                | World  |
| Horizontal Movement Unit  |   1 /   2 /   1 /   3 | 0          | 5      | horizontal unit movement                             | Unit   |
| Vertical Movement Unit    |   1 /   2 /   1 /   3 | 0          | 5      | vertical unit movement                               | Unit   |
| Horizontal Movement Item  | 100 / 120 / 100 / 150 | 0          | 5      | item horizontal movement * item weight               | Item   |
| Vertical Movement Item    | 100 / 120 / 100 / 150 | 0          | 5      | item horizontal movement * item weight               | Item   |
| Armor                     |  10 /  12 /   0 /  15 | 0          | 50     | none (hitpoints. if power falls to 0, unit is dead)  | None   |
| Sword                     |   1 /   2 /   1 /   3 | 3          | 20     | damage to other units armor                          | Item   |
| Power Generator           |   1 /   2 /   1 /   3 | 1          | 10     | power transferred to other item                      | Item   |
| Power Max. Value Upgrade  | 0 /   100 / 0 / 0     | 1          | 100    | power improvement of the other item * self.weight    | Item   |
| Power Refill Upgrade      | 0 /   500 / 0 / 0     | 1          | 500    | power refill improvement of other item * self.weight | Item   |
| Power Max. Refill Upgrade | 0 /   500 / 0 / 0     | 1          | 500    | power refill improvement of other item * self.weight | Item   |
| Radius Upgrade            | 0 /  1000 / 0 / 0     | 1          | 1000   | power improvement of the other item * self.weight    | Item   |
| Item Duplicator           | 0 /  1000 /   0 /   0 | 0          | 1000   | item.power + duplicator.weight * item.weight         | Item   |
| Unit Creator              | 0 / 10000 /   0 /   0 | 0          | 10000  | creator.weight                                       | Item   |

Power°: Starting Value / Max. Value / Refill to / Max. Refill

## Rule Set "Agents"

Idea: 
Model after Nature/Humans.
Based on [Sugarscape](https://en.wikipedia.org/wiki/Sugarscape)

##### Player
The task of the player is to tweek the code and settings of the agents in such a way as to allow his agents to perform better than the agents of the other players.

##### Tournaments
* Strength in numbers: 
  Each player starts on a empty map and tries to have the biggest possible agent population when the simulation finishes.
* Tribal wars:
  All players start on the same map. When the simulation finishes, the success of a player is measured by one of these:
  * The number of agents in the population.
  * The total amount of resources gathered over the whole simulation time.
  * The sum of resources possessed by the agents.
  * The total amount of resources spend over the whole simulation time.

##### Agent
Agents have a vision; they can move as far as they can see.
Agents have a metabolism: Each game round, they will loose the amount of resources of their metabolism. If the run out of resources, they die.
Agents have an age. Players can use the age to implement a fertility range and death of old age, if they like.
Agents can die, reproduce, move, gather all resources on the location they reside.
Agents can trade and fight.
