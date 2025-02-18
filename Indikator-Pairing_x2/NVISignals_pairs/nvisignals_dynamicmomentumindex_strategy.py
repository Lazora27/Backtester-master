import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
