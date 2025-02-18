import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
