import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_WyckoffWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und WyckoffWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'WyckoffWaveIndicator': 1.0
        })
    )
