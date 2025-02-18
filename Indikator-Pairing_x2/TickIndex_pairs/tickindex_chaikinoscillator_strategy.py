import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
