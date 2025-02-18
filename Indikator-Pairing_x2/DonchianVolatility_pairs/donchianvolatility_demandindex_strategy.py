import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und DemandIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'DemandIndex': 1.0
        })
    )
