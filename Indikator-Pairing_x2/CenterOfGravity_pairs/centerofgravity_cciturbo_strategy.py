import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und CCITurbo
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'CCITurbo': 1.0
        })
    )
