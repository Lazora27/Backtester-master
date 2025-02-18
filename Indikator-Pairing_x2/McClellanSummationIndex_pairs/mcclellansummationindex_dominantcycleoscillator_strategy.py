import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
