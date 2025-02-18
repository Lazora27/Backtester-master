import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'GannAngles': 1.0
        })
    )
