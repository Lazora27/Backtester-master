import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
