import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
