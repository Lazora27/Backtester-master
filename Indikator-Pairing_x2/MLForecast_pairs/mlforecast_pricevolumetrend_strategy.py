import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
