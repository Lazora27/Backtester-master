import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
