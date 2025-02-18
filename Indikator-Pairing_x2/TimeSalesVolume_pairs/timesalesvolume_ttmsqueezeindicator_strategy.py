import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_TTMSqueezeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und TTMSqueezeIndicator
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'TTMSqueezeIndicator': 1.0
        })
    )
