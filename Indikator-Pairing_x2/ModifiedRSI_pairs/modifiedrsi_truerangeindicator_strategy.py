import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
