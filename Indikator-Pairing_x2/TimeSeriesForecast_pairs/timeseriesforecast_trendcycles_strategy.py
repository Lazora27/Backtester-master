import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'TrendCycles': 1.0
        })
    )
