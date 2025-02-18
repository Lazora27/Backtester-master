import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'WolfeWaves': 1.0
        })
    )
