import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
