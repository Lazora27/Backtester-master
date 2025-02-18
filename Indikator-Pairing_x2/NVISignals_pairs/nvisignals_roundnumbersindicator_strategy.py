import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
