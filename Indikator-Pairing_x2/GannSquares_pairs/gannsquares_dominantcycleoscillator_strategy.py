import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
