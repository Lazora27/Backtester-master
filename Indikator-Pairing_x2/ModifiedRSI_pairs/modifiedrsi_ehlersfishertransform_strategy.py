import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
