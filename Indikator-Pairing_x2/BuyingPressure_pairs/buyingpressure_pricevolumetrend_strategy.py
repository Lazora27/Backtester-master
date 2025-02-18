import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
