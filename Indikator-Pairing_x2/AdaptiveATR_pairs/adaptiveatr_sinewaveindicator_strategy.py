import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
