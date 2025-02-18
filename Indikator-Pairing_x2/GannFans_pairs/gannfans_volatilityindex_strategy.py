import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VolatilityIndex': 1.0
        })
    )
