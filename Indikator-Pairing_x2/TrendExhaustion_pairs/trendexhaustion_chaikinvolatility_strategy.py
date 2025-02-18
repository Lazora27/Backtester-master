import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
