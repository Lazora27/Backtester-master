import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SmoothedCycle': 1.0
        })
    )
