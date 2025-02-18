import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
