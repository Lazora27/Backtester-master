import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'WeightedCycle': 1.0
        })
    )
