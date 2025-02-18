import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
