import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und GannSquares
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'GannSquares': 1.0
        })
    )
