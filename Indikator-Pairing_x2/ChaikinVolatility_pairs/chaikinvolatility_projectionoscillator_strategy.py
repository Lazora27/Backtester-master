import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
