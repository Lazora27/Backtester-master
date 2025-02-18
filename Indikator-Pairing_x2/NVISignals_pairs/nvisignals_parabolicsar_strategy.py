import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ParabolicSAR': 1.0
        })
    )
