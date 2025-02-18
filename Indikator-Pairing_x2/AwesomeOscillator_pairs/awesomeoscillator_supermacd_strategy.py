import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'SuperMACD': 1.0
        })
    )
