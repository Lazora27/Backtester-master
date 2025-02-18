import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und TimeCycle
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'TimeCycle': 1.0
        })
    )
