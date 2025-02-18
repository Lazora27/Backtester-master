import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
