import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
