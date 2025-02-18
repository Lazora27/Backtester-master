import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
