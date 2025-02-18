import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AverageTrueRange': 1.0
        })
    )
