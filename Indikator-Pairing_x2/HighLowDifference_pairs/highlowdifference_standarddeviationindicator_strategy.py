import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
