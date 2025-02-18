import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'HullMovingAverage': 1.0
        })
    )
