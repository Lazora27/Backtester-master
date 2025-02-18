import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
