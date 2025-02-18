import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DonchianVolatility': 1.0
        })
    )
