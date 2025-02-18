import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
