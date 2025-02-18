import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und NVISignals
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'NVISignals': 1.0
        })
    )
