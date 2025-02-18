import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
