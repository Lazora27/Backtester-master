import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
