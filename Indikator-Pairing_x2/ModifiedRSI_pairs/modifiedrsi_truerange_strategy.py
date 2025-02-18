import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TrueRange
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TrueRange': 1.0
        })
    )
