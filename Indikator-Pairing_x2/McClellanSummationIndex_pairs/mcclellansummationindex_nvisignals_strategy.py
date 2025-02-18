import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und NVISignals
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'NVISignals': 1.0
        })
    )
