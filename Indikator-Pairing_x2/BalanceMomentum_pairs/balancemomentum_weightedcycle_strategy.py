import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'WeightedCycle': 1.0
        })
    )
