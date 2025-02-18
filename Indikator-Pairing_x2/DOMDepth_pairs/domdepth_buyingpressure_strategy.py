import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'BuyingPressure': 1.0
        })
    )
