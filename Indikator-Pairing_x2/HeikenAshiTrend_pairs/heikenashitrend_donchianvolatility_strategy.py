import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'DonchianVolatility': 1.0
        })
    )
