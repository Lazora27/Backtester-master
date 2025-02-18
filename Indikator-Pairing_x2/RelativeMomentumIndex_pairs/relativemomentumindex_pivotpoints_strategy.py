import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
