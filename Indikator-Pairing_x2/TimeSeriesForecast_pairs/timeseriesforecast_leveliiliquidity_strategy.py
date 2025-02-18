import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
