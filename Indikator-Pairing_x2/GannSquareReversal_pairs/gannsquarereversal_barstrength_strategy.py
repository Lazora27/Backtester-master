import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und BarStrength
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'BarStrength': 1.0
        })
    )
