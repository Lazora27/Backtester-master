import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
