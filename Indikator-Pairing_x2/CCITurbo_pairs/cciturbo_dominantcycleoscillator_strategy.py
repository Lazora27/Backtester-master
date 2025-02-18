import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
