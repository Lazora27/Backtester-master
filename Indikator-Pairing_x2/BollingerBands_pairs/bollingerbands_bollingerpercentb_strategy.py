import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'BollingerPercentB': 1.0
        })
    )
