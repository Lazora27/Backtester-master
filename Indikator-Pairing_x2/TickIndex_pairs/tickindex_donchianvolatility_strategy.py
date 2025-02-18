import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
