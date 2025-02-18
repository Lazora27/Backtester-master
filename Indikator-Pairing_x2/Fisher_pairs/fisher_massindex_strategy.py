import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MassIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MassIndex': 1.0
        })
    )
