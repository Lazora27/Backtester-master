import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
