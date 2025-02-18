import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'LiquidityIndex': 1.0
        })
    )
