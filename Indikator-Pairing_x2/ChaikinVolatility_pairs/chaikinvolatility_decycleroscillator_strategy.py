import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
