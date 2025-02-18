import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
