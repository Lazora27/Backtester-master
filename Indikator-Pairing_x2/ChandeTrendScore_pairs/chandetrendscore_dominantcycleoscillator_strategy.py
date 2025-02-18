import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
