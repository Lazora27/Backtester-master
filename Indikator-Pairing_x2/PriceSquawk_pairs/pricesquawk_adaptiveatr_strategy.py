import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AdaptiveATR': 1.0
        })
    )
