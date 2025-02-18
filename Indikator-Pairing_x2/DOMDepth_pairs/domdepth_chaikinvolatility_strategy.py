import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
