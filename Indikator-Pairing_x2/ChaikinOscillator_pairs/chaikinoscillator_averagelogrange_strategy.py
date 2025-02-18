import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'AverageLogRange': 1.0
        })
    )
