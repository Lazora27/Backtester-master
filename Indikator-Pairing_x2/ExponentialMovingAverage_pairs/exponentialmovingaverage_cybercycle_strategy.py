import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'CyberCycle': 1.0
        })
    )
