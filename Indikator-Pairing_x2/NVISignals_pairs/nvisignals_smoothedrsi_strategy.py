import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SmoothedRSI': 1.0
        })
    )
