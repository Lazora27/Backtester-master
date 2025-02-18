import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
