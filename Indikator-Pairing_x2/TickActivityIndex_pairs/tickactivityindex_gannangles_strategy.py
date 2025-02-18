import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'GannAngles': 1.0
        })
    )
