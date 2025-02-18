import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
