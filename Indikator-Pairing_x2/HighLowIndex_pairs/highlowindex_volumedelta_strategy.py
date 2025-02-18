import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'VolumeDelta': 1.0
        })
    )
