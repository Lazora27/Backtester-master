import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BalanceMomentum': 1.0
        })
    )
