import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
