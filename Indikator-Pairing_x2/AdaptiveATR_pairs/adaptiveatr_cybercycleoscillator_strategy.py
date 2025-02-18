import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
