import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'DonchianChannels': 1.0
        })
    )
