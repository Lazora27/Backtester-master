import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'ProjectionBands': 1.0
        })
    )
