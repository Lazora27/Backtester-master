import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
