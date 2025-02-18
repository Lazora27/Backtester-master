import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und PriceDelta
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'PriceDelta': 1.0
        })
    )
