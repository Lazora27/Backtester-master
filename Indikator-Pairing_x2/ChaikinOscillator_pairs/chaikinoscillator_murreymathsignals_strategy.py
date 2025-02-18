import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
