import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'BollingerPercentB': 1.0
        })
    )
