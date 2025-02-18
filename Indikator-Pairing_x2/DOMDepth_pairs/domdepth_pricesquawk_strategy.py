import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'PriceSquawk': 1.0
        })
    )
