import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
