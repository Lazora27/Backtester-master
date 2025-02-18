import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
