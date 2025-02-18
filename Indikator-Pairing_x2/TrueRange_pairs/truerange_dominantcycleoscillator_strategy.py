import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
