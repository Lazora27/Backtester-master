import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'CenterOfGravity': 1.0
        })
    )
