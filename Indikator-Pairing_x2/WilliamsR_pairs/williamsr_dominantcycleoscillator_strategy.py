import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
