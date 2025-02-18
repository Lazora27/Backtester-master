import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
