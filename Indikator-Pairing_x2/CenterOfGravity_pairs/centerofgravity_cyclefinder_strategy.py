import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und CycleFinder
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'CycleFinder': 1.0
        })
    )
