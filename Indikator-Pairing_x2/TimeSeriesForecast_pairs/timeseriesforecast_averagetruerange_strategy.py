import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AverageTrueRange': 1.0
        })
    )
