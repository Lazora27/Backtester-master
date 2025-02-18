import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FisherTransform
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FisherTransform': 1.0
        })
    )
