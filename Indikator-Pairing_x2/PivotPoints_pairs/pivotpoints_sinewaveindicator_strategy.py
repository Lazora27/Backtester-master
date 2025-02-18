import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
