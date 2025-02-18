import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
