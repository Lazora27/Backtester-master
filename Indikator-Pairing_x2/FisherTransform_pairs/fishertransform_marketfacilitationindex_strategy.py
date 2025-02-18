import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
