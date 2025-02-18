import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
