import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
