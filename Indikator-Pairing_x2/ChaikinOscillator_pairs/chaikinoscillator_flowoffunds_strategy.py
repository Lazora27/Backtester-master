import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'FlowOfFunds': 1.0
        })
    )
