import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
