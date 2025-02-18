import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
