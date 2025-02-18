import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VolatilityIndex': 1.0
        })
    )
