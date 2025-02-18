import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
