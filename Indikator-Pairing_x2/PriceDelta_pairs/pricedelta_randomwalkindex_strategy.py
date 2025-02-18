import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
