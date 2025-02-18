import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
