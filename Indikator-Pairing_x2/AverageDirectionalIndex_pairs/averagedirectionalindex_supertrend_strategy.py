import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
