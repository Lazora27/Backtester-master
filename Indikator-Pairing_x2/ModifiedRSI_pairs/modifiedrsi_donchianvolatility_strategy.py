import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DonchianVolatility': 1.0
        })
    )
