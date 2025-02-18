import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
