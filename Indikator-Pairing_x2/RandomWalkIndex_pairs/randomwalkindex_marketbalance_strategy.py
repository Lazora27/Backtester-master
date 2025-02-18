import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
