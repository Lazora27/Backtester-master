import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
