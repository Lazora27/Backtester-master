import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
