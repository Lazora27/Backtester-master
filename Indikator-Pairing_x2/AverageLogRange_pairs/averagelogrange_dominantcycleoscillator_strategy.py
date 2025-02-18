import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
