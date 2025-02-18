import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'AdaptiveATR': 1.0
        })
    )
