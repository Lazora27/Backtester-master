import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
