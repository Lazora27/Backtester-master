import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
