import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'CycleFinder': 1.0
        })
    )
