import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
