import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'ConnorsRSI': 1.0
        })
    )
