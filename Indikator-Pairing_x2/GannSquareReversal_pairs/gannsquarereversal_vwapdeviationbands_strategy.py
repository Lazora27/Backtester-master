import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
