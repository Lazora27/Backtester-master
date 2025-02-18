import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
