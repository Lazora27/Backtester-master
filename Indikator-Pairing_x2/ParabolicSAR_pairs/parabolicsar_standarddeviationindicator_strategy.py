import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
