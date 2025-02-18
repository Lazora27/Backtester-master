import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
