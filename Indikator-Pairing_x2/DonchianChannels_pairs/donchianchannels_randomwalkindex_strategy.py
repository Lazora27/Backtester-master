import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
