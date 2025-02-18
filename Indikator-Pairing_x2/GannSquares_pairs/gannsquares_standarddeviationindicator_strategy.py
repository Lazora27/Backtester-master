import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
