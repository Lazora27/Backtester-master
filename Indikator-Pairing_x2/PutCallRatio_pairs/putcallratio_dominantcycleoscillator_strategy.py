import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
