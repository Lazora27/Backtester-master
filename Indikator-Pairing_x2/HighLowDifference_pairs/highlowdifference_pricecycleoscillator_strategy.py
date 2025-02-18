import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
