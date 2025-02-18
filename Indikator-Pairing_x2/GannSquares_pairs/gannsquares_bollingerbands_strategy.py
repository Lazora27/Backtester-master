import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und BollingerBands
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'BollingerBands': 1.0
        })
    )
