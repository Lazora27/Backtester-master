import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MACDHistogram': 1.0
        })
    )
