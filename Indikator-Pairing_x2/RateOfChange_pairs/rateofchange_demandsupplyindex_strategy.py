import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
