import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
