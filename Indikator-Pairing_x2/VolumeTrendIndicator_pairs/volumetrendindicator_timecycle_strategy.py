import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
