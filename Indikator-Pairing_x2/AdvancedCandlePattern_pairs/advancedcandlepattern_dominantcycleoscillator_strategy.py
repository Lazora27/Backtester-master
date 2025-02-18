import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
