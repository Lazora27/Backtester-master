import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
