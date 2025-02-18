import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und CycleFinder
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'CycleFinder': 1.0
        })
    )
