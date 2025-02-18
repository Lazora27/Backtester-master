import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
