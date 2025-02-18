import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
