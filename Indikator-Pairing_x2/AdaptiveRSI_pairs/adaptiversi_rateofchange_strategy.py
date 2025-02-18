import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und RateOfChange
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'RateOfChange': 1.0
        })
    )
