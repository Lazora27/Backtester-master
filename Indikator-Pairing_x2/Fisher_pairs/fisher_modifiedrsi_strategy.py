import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ModifiedRSI': 1.0
        })
    )
