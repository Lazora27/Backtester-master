import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
