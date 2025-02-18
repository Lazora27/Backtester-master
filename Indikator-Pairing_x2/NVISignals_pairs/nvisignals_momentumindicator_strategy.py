import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MomentumIndicator': 1.0
        })
    )
