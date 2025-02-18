import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'DonchianVolatility': 1.0
        })
    )
