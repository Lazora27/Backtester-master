import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
