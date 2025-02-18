import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
