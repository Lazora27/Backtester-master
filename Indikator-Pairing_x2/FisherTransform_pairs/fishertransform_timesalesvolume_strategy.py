import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
