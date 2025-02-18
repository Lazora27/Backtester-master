import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und RateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'RateOfChange': 1.0
        })
    )
