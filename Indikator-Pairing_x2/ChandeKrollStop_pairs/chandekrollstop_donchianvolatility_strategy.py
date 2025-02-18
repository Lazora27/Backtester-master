import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'DonchianVolatility': 1.0
        })
    )
