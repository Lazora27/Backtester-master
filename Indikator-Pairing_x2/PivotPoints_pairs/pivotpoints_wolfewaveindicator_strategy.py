import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
