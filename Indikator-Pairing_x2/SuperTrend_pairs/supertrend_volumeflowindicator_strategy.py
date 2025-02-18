import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
