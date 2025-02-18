import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
