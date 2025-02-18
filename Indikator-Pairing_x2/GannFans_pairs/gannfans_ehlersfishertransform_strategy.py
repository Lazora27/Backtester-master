import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
