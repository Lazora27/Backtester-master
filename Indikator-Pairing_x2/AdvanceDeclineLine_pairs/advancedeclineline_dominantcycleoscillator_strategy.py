import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
