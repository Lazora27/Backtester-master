import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
