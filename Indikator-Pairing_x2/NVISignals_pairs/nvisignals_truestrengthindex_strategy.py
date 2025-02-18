import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
