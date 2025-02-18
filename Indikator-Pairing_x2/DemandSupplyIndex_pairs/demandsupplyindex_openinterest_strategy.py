import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
