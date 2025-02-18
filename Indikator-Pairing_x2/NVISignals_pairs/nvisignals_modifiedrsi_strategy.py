import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ModifiedRSI': 1.0
        })
    )
