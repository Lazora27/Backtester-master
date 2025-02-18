import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
