import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'AverageLogRange': 1.0
        })
    )
