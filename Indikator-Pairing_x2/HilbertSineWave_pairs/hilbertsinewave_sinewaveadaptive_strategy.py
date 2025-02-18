import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
