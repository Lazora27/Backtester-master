import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AverageLogRange': 1.0
        })
    )
