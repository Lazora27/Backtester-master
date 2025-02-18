import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
