import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und MassIndex
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'MassIndex': 1.0
        })
    )
