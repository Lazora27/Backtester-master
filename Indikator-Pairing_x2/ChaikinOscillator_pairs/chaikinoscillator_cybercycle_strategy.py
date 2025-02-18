import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'CyberCycle': 1.0
        })
    )
