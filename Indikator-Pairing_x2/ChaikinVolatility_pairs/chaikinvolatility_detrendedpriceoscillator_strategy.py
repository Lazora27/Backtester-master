import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_DetrendedPriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und DetrendedPriceOscillator
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'DetrendedPriceOscillator': 1.0
        })
    )
