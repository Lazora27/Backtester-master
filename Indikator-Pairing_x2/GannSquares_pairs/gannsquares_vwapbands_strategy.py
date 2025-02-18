import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und VWAPBands
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'VWAPBands': 1.0
        })
    )
