import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FisherTransform
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FisherTransform': 1.0
        })
    )
