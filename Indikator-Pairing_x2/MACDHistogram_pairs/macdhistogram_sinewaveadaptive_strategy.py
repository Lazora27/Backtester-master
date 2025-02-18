import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
