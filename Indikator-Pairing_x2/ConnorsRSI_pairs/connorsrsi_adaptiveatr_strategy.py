import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AdaptiveATR': 1.0
        })
    )
