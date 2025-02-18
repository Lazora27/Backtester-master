import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
