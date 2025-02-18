import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und TrueRange
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'TrueRange': 1.0
        })
    )
