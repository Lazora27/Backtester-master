import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
