import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'DonchianVolatility': 1.0
        })
    )
