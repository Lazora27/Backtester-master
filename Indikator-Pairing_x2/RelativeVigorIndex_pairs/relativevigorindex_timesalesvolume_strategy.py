import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
