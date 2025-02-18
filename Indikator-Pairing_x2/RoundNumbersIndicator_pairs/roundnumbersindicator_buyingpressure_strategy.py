import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
