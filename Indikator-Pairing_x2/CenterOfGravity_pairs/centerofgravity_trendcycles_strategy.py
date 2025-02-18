import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'TrendCycles': 1.0
        })
    )
