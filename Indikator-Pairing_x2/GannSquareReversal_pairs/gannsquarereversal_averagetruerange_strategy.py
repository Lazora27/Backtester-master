import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AverageTrueRange': 1.0
        })
    )
