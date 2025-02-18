import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'DPOCycles': 1.0
        })
    )
