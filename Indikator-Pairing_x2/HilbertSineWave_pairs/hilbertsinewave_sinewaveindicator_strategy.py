import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
