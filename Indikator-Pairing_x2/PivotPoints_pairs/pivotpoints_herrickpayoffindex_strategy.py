import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
