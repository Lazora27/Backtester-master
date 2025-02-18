import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
