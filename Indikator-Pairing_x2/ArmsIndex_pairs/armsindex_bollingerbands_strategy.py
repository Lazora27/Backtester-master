import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
