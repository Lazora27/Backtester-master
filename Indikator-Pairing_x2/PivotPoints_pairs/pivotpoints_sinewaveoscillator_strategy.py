import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
