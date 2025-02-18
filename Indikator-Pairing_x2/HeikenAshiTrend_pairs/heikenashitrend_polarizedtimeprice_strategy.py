import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
