import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
