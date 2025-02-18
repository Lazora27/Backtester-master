import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'WeeklyCycle': 1.0
        })
    )
