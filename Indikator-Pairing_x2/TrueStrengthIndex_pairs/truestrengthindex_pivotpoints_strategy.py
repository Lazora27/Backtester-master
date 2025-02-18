import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
