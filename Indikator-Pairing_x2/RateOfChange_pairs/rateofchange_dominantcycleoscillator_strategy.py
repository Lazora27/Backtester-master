import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
