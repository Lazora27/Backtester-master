import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
