import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PivotPoints
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PivotPoints': 1.0
        })
    )
