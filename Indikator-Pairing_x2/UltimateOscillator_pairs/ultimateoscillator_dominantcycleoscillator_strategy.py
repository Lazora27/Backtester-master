import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
