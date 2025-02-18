import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MomentumIndicator': 1.0
        })
    )
