import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'AdaptiveATR': 1.0
        })
    )
