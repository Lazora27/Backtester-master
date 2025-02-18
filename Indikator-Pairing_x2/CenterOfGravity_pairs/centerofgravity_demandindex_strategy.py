import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und DemandIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'DemandIndex': 1.0
        })
    )
