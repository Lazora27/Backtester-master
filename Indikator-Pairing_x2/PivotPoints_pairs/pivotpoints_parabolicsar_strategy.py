import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ParabolicSAR': 1.0
        })
    )
