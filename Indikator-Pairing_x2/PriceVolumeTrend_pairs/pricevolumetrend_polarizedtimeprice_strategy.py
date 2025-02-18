import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
