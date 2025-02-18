import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'IchimokuCloud': 1.0
        })
    )
