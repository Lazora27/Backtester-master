import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TRIXIndicator': 1.0
        })
    )
