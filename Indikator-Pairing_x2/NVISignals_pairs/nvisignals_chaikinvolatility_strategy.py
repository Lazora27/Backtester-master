import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
