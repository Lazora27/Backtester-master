import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
