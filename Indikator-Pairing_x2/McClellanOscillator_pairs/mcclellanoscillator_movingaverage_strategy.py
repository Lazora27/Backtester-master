import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MovingAverage': 1.0
        })
    )
