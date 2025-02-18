import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SuperTrend': 1.0
        })
    )
