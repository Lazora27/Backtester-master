import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'TrendExhaustion': 1.0
        })
    )
