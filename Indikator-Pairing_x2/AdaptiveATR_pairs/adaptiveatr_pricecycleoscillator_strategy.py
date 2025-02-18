import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
