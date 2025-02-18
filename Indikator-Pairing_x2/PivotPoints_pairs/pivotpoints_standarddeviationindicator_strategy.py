import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
