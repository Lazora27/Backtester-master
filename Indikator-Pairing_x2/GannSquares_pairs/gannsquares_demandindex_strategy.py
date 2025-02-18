import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und DemandIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'DemandIndex': 1.0
        })
    )
