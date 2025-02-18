import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
