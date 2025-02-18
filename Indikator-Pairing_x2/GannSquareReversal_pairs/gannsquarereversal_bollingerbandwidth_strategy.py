import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
