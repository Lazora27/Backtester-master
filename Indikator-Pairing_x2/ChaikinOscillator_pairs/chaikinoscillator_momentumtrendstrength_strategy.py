import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
