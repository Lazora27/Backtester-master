import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
