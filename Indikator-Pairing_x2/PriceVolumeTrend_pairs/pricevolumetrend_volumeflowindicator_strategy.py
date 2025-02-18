import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
