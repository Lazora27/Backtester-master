import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
