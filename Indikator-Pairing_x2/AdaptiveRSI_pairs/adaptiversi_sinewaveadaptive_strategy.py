import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
