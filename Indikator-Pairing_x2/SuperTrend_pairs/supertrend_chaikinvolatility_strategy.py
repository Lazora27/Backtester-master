import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
