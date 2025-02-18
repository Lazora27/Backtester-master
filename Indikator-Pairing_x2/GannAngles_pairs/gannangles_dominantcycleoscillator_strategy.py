import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
