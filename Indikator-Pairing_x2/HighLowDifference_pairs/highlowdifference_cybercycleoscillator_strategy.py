import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
