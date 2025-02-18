import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'GannAngles': 1.0
        })
    )
