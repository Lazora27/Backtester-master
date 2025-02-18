import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
