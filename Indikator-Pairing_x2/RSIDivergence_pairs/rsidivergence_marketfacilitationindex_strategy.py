import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
