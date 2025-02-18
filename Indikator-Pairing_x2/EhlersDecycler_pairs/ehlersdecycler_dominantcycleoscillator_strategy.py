import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
