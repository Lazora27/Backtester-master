import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
