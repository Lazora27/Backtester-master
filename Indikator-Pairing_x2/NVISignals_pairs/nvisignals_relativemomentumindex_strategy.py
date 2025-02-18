import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
