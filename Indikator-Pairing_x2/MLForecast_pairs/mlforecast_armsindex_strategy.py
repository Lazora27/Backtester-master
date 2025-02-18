import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ArmsIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ArmsIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ArmsIndex': 1.0
        })
    )
