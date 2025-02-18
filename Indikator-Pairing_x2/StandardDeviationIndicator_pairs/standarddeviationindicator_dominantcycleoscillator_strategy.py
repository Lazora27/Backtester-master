import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
