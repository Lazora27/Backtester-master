import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeAccumulationPercentage_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeAccumulationPercentage und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'VolumeAccumulationPercentage': 1.0,
            'SmoothedCycle': 1.0
        })
    )
