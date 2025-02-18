import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
