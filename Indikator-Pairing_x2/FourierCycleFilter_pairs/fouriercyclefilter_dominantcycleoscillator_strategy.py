import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
