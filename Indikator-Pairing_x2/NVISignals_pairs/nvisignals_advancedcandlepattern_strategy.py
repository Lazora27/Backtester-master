import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
