import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
