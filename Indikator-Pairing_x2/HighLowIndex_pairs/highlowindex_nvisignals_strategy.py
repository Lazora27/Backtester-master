import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und NVISignals
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'NVISignals': 1.0
        })
    )
