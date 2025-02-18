import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AroonIndicator': 1.0
        })
    )
