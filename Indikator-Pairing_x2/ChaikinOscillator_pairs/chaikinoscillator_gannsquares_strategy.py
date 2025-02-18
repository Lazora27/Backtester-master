import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
