import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
