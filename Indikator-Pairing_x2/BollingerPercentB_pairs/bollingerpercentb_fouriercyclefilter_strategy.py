import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
