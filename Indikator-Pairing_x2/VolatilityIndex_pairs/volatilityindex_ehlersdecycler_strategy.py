import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
