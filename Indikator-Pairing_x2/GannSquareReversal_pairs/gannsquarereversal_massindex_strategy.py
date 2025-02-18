import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und MassIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'MassIndex': 1.0
        })
    )
