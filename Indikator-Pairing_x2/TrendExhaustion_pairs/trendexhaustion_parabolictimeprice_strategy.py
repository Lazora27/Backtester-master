import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
