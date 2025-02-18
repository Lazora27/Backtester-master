import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'DonchianVolatility': 1.0
        })
    )
