import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
