import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
