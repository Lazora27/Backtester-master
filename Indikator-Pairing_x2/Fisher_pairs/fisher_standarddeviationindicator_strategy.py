import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
