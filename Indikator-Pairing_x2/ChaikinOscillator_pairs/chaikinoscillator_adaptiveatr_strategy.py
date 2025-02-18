import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'AdaptiveATR': 1.0
        })
    )
