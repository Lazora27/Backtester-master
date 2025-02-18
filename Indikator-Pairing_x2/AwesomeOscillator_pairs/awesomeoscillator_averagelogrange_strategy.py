import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'AverageLogRange': 1.0
        })
    )
