import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
