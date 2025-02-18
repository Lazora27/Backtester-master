import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
