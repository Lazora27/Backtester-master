import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VolatilityIndex': 1.0
        })
    )
