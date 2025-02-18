import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
