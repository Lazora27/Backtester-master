import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'UlcerIndex': 1.0
        })
    )
