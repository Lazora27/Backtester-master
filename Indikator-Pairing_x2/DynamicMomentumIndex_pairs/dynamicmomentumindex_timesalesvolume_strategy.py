import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
