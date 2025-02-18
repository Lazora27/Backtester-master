import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
