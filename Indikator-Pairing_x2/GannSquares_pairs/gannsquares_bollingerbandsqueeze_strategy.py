import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
