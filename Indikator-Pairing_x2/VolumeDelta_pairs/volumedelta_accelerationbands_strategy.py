import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AccelerationBands': 1.0
        })
    )
