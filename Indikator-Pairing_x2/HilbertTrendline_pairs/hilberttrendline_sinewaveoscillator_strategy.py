import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
