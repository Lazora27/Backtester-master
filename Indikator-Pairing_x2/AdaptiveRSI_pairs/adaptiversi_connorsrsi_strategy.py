import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ConnorsRSI': 1.0
        })
    )
