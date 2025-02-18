import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
