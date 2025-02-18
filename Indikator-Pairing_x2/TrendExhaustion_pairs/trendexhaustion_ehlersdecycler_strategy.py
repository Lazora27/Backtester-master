import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'EhlersDecycler': 1.0
        })
    )
