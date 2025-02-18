import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AdaptiveATR': 1.0
        })
    )
