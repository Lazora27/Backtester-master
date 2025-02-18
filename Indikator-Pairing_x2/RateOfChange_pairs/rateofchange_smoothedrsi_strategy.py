import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SmoothedRSI': 1.0
        })
    )
