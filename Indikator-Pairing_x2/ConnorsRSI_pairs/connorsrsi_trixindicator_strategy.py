import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TRIXIndicator': 1.0
        })
    )
