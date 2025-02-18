import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'MovingAverage': 1.0
        })
    )
