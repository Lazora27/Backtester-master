import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und CCITurbo
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'CCITurbo': 1.0
        })
    )
