import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
