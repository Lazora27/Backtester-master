import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'FearGreedIndex': 1.0
        })
    )
