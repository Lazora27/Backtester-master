import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
