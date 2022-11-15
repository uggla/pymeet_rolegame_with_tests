#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import character
import game

def main():
    name = input("Enter your hero name: ")
    player = character.Player(name)
    mygame = game.Game(player)

    print("Here are your player initial stats:")
    player.display_characteristics()
    # Do the fucking loop
    while not mygame.is_over():
        player.display_position()
        mygame.get_player_action()
        # fight or not ?
        player.display_characteristics()
        break

if __name__ == "__main__":
    main()
