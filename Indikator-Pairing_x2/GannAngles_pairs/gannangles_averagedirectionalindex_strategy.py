import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
