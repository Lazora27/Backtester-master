import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'BuyingPressure': 1.0
        })
    )
