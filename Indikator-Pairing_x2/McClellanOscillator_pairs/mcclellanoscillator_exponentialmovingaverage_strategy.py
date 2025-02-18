import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
