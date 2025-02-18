import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
