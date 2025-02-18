import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
