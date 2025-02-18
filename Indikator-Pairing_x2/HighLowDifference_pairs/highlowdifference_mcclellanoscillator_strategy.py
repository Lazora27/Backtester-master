import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_McClellanOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und McClellanOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'McClellanOscillator': 1.0
        })
    )
