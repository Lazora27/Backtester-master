import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'MACDHistogram': 1.0
        })
    )
