import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
