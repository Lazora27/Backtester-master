import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
