import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'CCITurbo': 1.0
        })
    )
