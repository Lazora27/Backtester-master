import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
