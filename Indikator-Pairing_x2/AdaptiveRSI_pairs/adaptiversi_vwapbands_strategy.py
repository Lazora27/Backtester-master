import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und VWAPBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'VWAPBands': 1.0
        })
    )
