import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
