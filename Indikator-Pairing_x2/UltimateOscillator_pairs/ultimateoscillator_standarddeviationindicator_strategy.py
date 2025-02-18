import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
