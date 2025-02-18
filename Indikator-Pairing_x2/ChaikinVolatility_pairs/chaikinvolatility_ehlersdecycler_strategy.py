import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'EhlersDecycler': 1.0
        })
    )
