import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
