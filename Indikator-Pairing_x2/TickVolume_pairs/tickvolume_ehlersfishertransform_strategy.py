import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
