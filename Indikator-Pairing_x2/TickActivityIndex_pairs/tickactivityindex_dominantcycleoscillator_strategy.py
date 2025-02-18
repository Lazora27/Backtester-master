import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
