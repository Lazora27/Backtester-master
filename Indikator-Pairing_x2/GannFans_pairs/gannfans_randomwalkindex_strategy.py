import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
