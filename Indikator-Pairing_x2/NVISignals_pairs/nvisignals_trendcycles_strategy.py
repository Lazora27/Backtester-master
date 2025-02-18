import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TrendCycles
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TrendCycles': 1.0
        })
    )
