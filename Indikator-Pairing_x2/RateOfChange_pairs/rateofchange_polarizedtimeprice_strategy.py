import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
