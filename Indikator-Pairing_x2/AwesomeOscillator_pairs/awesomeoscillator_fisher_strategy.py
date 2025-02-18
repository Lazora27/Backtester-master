import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und Fisher
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'Fisher': 1.0
        })
    )
