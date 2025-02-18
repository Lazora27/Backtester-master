import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und MassIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'MassIndex': 1.0
        })
    )
