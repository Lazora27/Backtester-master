import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und BollingerBands
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'BollingerBands': 1.0
        })
    )
