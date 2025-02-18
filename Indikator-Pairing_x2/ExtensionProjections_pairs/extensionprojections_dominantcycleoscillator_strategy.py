import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
