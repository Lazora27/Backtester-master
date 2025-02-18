import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HullMovingAverage': 1.0
        })
    )
