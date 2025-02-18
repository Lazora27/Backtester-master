import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
