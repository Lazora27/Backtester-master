import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
