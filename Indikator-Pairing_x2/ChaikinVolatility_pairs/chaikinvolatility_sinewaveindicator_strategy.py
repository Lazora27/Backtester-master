import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
