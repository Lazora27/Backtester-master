import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
