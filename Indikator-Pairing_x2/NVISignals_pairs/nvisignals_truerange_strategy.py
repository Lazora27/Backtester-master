import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TrueRange
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TrueRange': 1.0
        })
    )
