import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
