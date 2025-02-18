import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'GannSquareReversal': 1.0
        })
    )
