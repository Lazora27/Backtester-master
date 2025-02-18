import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'PivotPoints': 1.0
        })
    )
