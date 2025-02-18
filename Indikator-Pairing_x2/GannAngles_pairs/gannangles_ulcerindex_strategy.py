import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'UlcerIndex': 1.0
        })
    )
