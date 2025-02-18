import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSineWave_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSineWave und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HilbertSineWave': {
                'class': HilbertSineWave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSineWave'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HilbertSineWave': 1.0,
            'HilbertSinewave': 1.0
        })
    )
