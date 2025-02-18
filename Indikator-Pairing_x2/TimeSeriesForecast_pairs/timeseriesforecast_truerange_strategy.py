import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und TrueRange
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'TrueRange': 1.0
        })
    )
