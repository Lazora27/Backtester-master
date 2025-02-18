import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
