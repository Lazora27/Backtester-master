import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'StochasticRSI': 1.0
        })
    )
