import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CumulativeTick': 1.0
        })
    )
