import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
