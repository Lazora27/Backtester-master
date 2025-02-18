import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
