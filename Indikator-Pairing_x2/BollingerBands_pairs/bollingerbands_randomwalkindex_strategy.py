import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
