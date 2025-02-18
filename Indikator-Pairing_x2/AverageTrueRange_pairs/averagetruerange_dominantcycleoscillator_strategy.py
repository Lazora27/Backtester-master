import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
