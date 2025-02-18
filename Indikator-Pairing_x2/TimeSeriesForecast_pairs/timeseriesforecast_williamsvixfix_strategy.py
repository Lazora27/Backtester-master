import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
