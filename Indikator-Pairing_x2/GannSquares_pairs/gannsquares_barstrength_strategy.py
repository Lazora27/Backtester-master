import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und BarStrength
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'BarStrength': 1.0
        })
    )
