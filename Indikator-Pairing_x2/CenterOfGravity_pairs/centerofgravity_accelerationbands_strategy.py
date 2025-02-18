import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'AccelerationBands': 1.0
        })
    )
