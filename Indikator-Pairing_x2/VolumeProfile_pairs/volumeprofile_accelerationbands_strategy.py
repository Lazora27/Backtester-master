import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'AccelerationBands': 1.0
        })
    )
