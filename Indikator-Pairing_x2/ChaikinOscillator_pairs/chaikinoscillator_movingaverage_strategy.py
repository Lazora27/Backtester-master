import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MovingAverage': 1.0
        })
    )
