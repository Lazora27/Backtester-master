import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
