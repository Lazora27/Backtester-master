import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
