import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VortexIndicator': 1.0
        })
    )
