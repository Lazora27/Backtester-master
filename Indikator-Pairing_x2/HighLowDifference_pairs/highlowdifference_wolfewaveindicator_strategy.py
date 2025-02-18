import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
