import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
