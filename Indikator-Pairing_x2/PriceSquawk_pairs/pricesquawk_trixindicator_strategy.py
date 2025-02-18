import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TRIXIndicator': 1.0
        })
    )
