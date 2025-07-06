from mahjong.hand_calculating.hand import HandCalculator
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.hand_calculating.hand_response import HandResponse
from mahjong.meld import Meld
from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter
from mahjong.constants import DISPLAY_WINDS

calculator = HandCalculator()


# useful helper
def print_hand_result(hand_result: HandResponse, config: HandConfig) -> None:

    


    print(f"You are {DISPLAY_WINDS[config.player_wind]} ")

    if DISPLAY_WINDS[config.player_wind]=="East":
        print(f"Each player pays {hand_result.cost['main']} and the bonus is {hand_result.cost['main_bonus']}")

        print(f"The additional points are {hand_result.cost['additional']} and the additional bonus is {hand_result.cost['additional_bonus']}")

        print(f"The kyoutakuyakus are {hand_result.yaku} and the yaku level is {hand_result.cost['yaku_level']} ")
        
        print(f"The kyoutaku is {hand_result.cost['kyoutaku_bonus']} and the total result is {hand_result.cost['total']} ")

    else:
        print(f"Each non-east player pays {hand_result.cost['additional']}.\nEast pays {hand_result.cost['main']}")

        print(f"The bonus is {hand_result.cost['main_bonus']}")

        print(f"The additional points are {hand_result.cost['additional']} and the additional bonus is {hand_result.cost['additional_bonus']}")

        print(f"The kyoutakuyakus are {hand_result.yaku} and the yaku level is {hand_result.cost['yaku_level']} ")
        
        print(f"The kyoutaku is {hand_result.cost['kyoutaku_bonus']} and the total result is {hand_result.cost['total']} ")
    # print(hand_result.han, hand_result.fu)
    # print(hand_result.cost["main"]})
    # print(hand_result.cost["main_bonus"])
    # print(hand_result.cost["additional"])
    # print(hand_result.cost["additional_bonus"])
    # print(hand_result.cost["kyoutaku_bonus"])
    # print(hand_result.cost["total"])
    # print(hand_result.cost["yaku_level"])
    # print(hand_result.yaku)
    for fu_item in hand_result.fu_details:
        print(fu_item)
    print("")


# ####################################################################
# # Tanyao hand by ron                                               #
# ####################################################################


# # we had to use all 14 tiles in that array
# tiles = TilesConverter.string_to_136_array(man="22444", pin="333567", sou="444")
# win_tile = TilesConverter.string_to_136_array(sou="4")[0]

# result = calculator.estimate_hand_value(tiles, win_tile)
# print_hand_result(result)


# ####################################################################
# # Tanyao hand by tsumo                                             #
# ####################################################################


# result = calculator.estimate_hand_value(tiles, win_tile, config=HandConfig(is_tsumo=True))
# print_hand_result(result)


# ####################################################################
# # Add open set to hand                                             #
# ####################################################################


# melds = [Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(man="444"))]

# result = calculator.estimate_hand_value(
#     tiles, win_tile, melds=melds, config=HandConfig(options=OptionalRules(has_open_tanyao=True))
# )
# print_hand_result(result)


# ####################################################################
# # Shanten calculation                                              #
# ####################################################################


# shanten = Shanten()
# tiles = TilesConverter.string_to_34_array(man="13569", pin="123459", sou="443")
# result = shanten.calculate_shanten(tiles)

# print(result)

# ####################################################################
# # Kazoe as a sanbaiman                                             #
# ####################################################################


# tiles = TilesConverter.string_to_136_array(man="222244466677788")
# win_tile = TilesConverter.string_to_136_array(man="7")[0]
# melds = [Meld(Meld.KAN, TilesConverter.string_to_136_array(man="2222"), False)]

# dora_indicators = [
#     TilesConverter.string_to_136_array(man="1")[0],
#     TilesConverter.string_to_136_array(man="1")[0],
#     TilesConverter.string_to_136_array(man="1")[0],
#     TilesConverter.string_to_136_array(man="1")[0],
# ]

# config = HandConfig(is_riichi=True, options=OptionalRules(kazoe_limit=HandConfig.KAZOE_SANBAIMAN))
# result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
# print_hand_result(result)


# ####################################################################
# # Change the cost of yaku                                          #
# ####################################################################


# config = HandConfig(is_renhou=True)
# # renhou as an yakuman - old style
# config.yaku.renhou.han_closed = 13

# tiles = TilesConverter.string_to_136_array(man="22444", pin="333567", sou="444")
# win_tile = TilesConverter.string_to_136_array(sou="4")[0]

# result = calculator.estimate_hand_value(tiles, win_tile, config=config)
# print_hand_result(result)

####################################################################
# claras hand                                               #
####################################################################


# we had to use all 14 tiles in that array
tiles = TilesConverter.string_to_136_array(man="222234", pin="11",honors="444777")
win_tile = TilesConverter.string_to_136_array(man="4")[0]
myconfig=HandConfig(is_tsumo=False,player_wind=27)

result = calculator.estimate_hand_value(tiles, win_tile,None,None,myconfig)
print_hand_result(result,myconfig)
print(result.cost.keys())
