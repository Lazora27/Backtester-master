import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
