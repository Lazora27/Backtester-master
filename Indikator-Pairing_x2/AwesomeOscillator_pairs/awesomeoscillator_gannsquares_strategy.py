import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
