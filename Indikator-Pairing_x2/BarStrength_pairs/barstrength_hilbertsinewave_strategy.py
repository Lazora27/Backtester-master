import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'HilbertSinewave': 1.0
        })
    )
