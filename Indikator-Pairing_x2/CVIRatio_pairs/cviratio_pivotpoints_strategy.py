import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PivotPoints
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PivotPoints': 1.0
        })
    )
