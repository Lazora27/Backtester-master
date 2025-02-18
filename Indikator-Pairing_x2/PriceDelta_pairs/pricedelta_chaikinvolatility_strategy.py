import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
