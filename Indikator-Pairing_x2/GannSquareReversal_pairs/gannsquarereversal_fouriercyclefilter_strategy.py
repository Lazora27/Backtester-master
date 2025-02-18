import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
