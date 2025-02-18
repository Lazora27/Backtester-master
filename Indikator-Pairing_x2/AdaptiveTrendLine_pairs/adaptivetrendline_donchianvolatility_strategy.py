import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'DonchianVolatility': 1.0
        })
    )
