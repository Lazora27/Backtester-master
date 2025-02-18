import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
