import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und CycleFinder
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'CycleFinder': 1.0
        })
    )
