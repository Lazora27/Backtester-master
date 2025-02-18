import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
