import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
