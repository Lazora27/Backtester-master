import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
