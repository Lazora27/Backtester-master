import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
