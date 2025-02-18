import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und BarStrength
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'BarStrength': 1.0
        })
    )
