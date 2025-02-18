import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MurreyMathLines': 1.0
        })
    )
