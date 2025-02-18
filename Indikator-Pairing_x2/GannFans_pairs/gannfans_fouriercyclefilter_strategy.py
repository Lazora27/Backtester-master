import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
