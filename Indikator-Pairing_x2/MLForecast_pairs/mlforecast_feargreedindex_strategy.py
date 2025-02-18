import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FearGreedIndex': 1.0
        })
    )
