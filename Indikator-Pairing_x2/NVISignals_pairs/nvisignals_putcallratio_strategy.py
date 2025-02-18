import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PutCallRatio': 1.0
        })
    )
