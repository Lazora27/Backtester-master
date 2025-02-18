import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeVolumeIndex_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeVolumeIndex und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'CumulativeVolumeIndex': 1.0,
            'SmoothedCycle': 1.0
        })
    )
