import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und DemandIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'DemandIndex': 1.0
        })
    )
