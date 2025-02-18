import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
