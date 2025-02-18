import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'PivotPoints': 1.0
        })
    )
