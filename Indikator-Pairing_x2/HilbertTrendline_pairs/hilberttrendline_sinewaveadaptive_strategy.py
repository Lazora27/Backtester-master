import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendline_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendline und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HilbertTrendline': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
