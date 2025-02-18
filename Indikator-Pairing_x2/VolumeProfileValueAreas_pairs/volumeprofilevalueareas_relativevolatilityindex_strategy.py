import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfileValueAreas_RelativeVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfileValueAreas und RelativeVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            },
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            }
        }),
        ('weights', {
            'VolumeProfileValueAreas': 1.0,
            'RelativeVolatilityIndex': 1.0
        })
    )
