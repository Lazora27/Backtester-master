import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'PriceSquawk': 1.0
        })
    )
