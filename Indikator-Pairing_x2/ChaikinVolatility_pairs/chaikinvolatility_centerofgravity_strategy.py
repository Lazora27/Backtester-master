import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'CenterOfGravity': 1.0
        })
    )
