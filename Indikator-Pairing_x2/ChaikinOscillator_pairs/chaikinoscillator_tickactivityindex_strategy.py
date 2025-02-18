import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'TickActivityIndex': 1.0
        })
    )
