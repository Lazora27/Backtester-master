import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
