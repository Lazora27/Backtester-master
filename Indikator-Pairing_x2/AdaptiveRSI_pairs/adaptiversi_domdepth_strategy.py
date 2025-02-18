import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und DOMDepth
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'DOMDepth': 1.0
        })
    )
