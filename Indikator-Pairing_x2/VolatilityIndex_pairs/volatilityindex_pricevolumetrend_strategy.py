import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
