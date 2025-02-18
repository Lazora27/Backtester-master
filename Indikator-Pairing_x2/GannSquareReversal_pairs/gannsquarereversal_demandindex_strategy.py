import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und DemandIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'DemandIndex': 1.0
        })
    )
