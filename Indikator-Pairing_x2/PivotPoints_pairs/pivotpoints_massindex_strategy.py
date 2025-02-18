import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und MassIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'MassIndex': 1.0
        })
    )
