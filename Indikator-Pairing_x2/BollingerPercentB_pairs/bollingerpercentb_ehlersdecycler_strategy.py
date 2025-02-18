import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'EhlersDecycler': 1.0
        })
    )
