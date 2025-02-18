import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'HilbertSinewave': 1.0
        })
    )
