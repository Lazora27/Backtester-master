import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'ProjectionBands': 1.0
        })
    )
