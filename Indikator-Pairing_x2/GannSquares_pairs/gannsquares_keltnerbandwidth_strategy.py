import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
