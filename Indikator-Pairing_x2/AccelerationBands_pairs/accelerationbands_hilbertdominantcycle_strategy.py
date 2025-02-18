import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
